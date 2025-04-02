from fastapi import FastAPI
from app.routes import item
from app.database import engine, create_database
from app.models import item as item_model

# Create the database if it doesn't exist
create_database()

# Create tables
item_model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Item Management API",
    description="FastAPI application for managing items",
    version="1.0.0"
)

app.include_router(item.router, prefix="/api/v1")
