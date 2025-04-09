from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.user import User, LoginActivity
from app.schemas.user import UserCreate, UserResponse, UserLogin, UserUpdate, OTPVerification, RoleUpdate, LoginActivityResponse
from passlib.context import CryptContext
import random
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserLogin, ResetPasswordRequest, ResetPasswordConfirm
from email_validator import validate_email, EmailNotValidError

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

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
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == form_data.username).first()
    if not db_user or not pwd_context.verify(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

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

@router.post("/reset-password-request")
def reset_password_request(email: str, db: Session = Depends(get_db)):
    try:
        validate_email(email)
    except EmailNotValidError:
        raise HTTPException(status_code=400, detail="Invalid email address")
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    # Simulate sending a reset token (e.g., via email)
    reset_token = "reset-token-placeholder"  # Replace with actual token generation logic
    return {"message": "Password reset token sent", "reset_token": reset_token}

@router.post("/reset-password-confirm")
def reset_password_confirm(data: ResetPasswordConfirm, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == data.email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if data.reset_token != "reset-token-placeholder":  # Replace with actual token validation
        raise HTTPException(status_code=400, detail="Invalid reset token")
    db_user.hashed_password = pwd_context.hash(data.new_password)
    db.commit()
    return {"message": "Password reset successfully"}