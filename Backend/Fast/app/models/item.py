from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Specify length for VARCHAR
    description = Column(String(1024))      # Specify length for VARCHAR
    price = Column(Float)
