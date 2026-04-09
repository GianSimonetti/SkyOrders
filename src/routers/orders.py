from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.dependencies import get_db
from src.schemas import OrderCreate, OrderResponse
from src.services import create_order_service, get_orders_service

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("/", response_model=list[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return get_orders_service(db)


@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order_service(db, order)