from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.user import User, LoginActivity
from app.schemas.user import UserCreate, UserResponse, UserLogin, UserUpdate, OTPVerification, RoleUpdate, LoginActivityResponse
from passlib.context import CryptContext
import random

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if the username already exists
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Check if the email already exists
    existing_email = db.query(User).filter(User.email == user.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def login_user(user: UserLogin, request: Request, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    # Track login activity
    ip_address = request.client.host
    login_activity = LoginActivity(user_id=db_user.id, ip_address=ip_address)
    db.add(login_activity)
    db.commit()
    return {"message": "Login successful"}

@router.put("/update", response_model=UserResponse)
def update_user(user_update: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_update.id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user_update.username:
        db_user.username = user_update.username
    if user_update.email:
        db_user.email = user_update.email
    db.commit()
    db.refresh(db_user)
    return db_user

@router.put("/change-password")
def change_password(user_update: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_update.id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user_update.password:
        db_user.hashed_password = pwd_context.hash(user_update.password)
        db.commit()
        return {"message": "Password changed successfully"}
    
    raise HTTPException(status_code=400, detail="New password not provided")

@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

@router.post("/verify-email")
def verify_email(otp_data: OTPVerification, db: Session = Depends(get_db)):
    # Simulate OTP verification logic
    db_user = db.query(User).filter(User.email == otp_data.email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if otp_data.otp != "123456":  # Replace with actual OTP logic
        raise HTTPException(status_code=400, detail="Invalid OTP")
    return {"message": "Email verified successfully"}

@router.put("/update-role")
def update_role(role_update: RoleUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == role_update.user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.role = role_update.role
    db.commit()
    return {"message": f"Role updated to {role_update.role}"}

@router.get("/login-activities", response_model=List[LoginActivityResponse])
def get_login_activities(user_id: int, db: Session = Depends(get_db)):
    return db.query(LoginActivity).filter(LoginActivity.user_id == user_id).all()