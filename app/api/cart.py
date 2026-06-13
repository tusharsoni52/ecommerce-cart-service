from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.cart import CartItemCreate, CartItemResponse
from app.services.cart_service import (
    add_to_cart,
    get_cart_by_customer
)

router = APIRouter(tags=["Cart"])


@router.post(
    "/cart",
    response_model=CartItemResponse
)
def create_cart_item(
        cart_item: CartItemCreate,
        db: Session = Depends(get_db)
):
    return add_to_cart(db, cart_item)


@router.get(
    "/cart/{customer_id}",
    response_model=List[CartItemResponse]
)
def get_customer_cart(
        customer_id: int,
        db: Session = Depends(get_db)
):
    return get_cart_by_customer(db, customer_id)