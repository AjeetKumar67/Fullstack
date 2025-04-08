from fastapi import FastAPI
from app.routes import order
from app.database import engine, create_database
from app.models import order as order_model

# Ensure the database is created
create_database()

# Create tables
order_model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Order Management API",
    description="FastAPI application for managing orders",
    version="1.0.0"
)

app.include_router(order.router, prefix="/api/v1")
