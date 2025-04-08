from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(255), index=True)
    quantity = Column(Integer)
    total_price = Column(Float)
