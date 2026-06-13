from pydantic import BaseModel


class CartItemCreate(BaseModel):
    customer_id: int
    product_id: int
    quantity: int


class CartItemResponse(BaseModel):
    id: int
    customer_id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True