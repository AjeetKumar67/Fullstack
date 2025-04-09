from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date, datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    photo: Optional[str] = None
    dob: Optional[date] = None
    mobile_number: Optional[str] = None
    address: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # Updated for Pydantic v2

class UserUpdate(UserBase):
    password: str = None  # Password is optional for updates

class OTPVerification(BaseModel):
    email: EmailStr
    otp: str

class RoleUpdate(BaseModel):
    user_id: int
    role: str

class LoginActivityResponse(BaseModel):
    id: int
    user_id: int
    login_time: datetime
    ip_address: str

    class Config:
        from_attributes = True  # Updated for Pydantic v2

class ResetPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordConfirm(BaseModel):
    email: EmailStr
    reset_token: str
    new_password: str