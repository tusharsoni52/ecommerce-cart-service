import requests

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.config import settings
from app.models.cart import CartItem
from app.schemas.cart import CartItemCreate


def add_to_cart(db: Session, cart_item: CartItemCreate):
    response = requests.get(
        f"{settings.PRODUCT_SERVICE_URL}/api/v1/products/{cart_item.product_id}"
    )
    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db_item = CartItem(
        customer_id=cart_item.customer_id,
        product_id=cart_item.product_id,
        quantity=cart_item.quantity
    )

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def get_cart_by_customer(db: Session, customer_id: int):
    return (
        db.query(CartItem)
        .filter(CartItem.customer_id == customer_id)
        .all()
    )


def checkout(db: Session, customer_id: int):
    cart_items = (
        db.query(CartItem)
        .filter(CartItem.customer_id == customer_id)
        .all()
    )

    if not cart_items:
        raise HTTPException(
            status_code=404,
            detail="Cart is empty"
        )

    total_amount = 0

    for item in cart_items:
        product_response = requests.get(
            f"{settings.PRODUCT_SERVICE_URL}/api/v1/products/{item.product_id}"
        )
        if product_response.status_code != 200:
            raise HTTPException(
                status_code=404,
                detail=f"Product {item.product_id} not found"
            )
        product = product_response.json()
        total_amount += float(product["price"]) * item.quantity

    order_response = requests.post(
        f"{settings.ORDER_SERVICE_URL}/api/v1/orders",
        json={
            "customer_id": customer_id,
            "total_amount": total_amount,
            "status": "PLACED"
        }
    )

    if order_response.status_code != 200:
        raise HTTPException(
            status_code=500,
            detail="Failed to create order"
        )

    db.query(CartItem) \
        .filter(CartItem.customer_id == customer_id) \
        .delete()

    db.commit()

    return {
        "message": "Checkout successful",
        "order": order_response.json()
    }