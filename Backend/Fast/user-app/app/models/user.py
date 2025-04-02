from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(128))
    full_name = Column(String(100), nullable=True)
    photo = Column(String(255), nullable=True)
    dob = Column(Date, nullable=True)
    mobile_number = Column(String(15), nullable=True)
    address = Column(String(255), nullable=True)
    role = Column(String(50), default="user")  # Default role is 'user'
    login_activities = relationship("LoginActivity", back_populates="user")

class LoginActivity(Base):
    __tablename__ = "login_activities"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    login_time = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String(45))  # IPv4/IPv6 compatible
    user = relationship("User", back_populates="login_activities")