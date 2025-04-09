from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from app.routes import user
from app.database import engine, create_database
from app.models import user as user_model

# Create the database if it doesn't exist
create_database()

# Create tables
user_model.Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/login")

app = FastAPI(
    title="User Management API",
    description="FastAPI application for managing users",
    version="1.0.0"
)

app.include_router(user.router, prefix="/api/v1")