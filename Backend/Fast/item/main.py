from fastapi import FastAPI
from .routes import item  # Use relative import
from .database import engine, create_database  # Use relative import
from .models import item as item_model  # Use relative import

# Ensure the database is created
create_database()

# Create tables
item_model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Item Management API",
    description="FastAPI application for managing items",
    version="1.0.0"
)

app.include_router(item.router, prefix="/api/v1")
