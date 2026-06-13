from sqlalchemy.orm import Session

from app.models.cart import CartItem
from app.schemas.cart import CartItemCreate


def add_to_cart(db: Session, cart_item: CartItemCreate):
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