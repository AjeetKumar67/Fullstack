from pydantic import BaseModel

class OrderBase(BaseModel):
    item_name: str
    quantity: int
    total_price: float

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int

    class Config:
        from_attributes = True
