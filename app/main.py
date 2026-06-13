from fastapi import FastAPI

from app.api.cart import router as cart_router
from app.config import settings
from app.db.database import Base, engine
from app.models.cart import CartItem

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(cart_router)


@app.get("/health")
def health():
    return {
        "status": "UP",
        "service": "cart-service"
    }