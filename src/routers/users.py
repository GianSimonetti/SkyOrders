from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.dependencies import get_db
from src.models import User
from src.schemas import UserWithOrders, OrderResponse, UserCreate, UserResponse
from src.security import get_current_user
from src.services import (
    get_users_service,
    create_user_service,
    update_user_service,
    delete_user_service,
    get_orders_by_user_service,
    get_user_with_orders_service
)


router = APIRouter()

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return get_users_service(db)


@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(db, user)


@router.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user_service(db, user_id, user)


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user_service(db, user_id)

@router.get("/users/{user_id}/orders", response_model=list[OrderResponse])
def get_orders_by_user(user_id: int, db: Session = Depends(get_db)):
    return get_orders_by_user_service(db, user_id)

@router.get("/users/{user_id}/full", response_model=UserWithOrders)
def get_user_with_orders(user_id: int, db: Session = Depends(get_db)):
    return get_user_with_orders_service(db, user_id)

@router.get("/users/me", response_model=UserResponse)
def get_me(user_id: int = Depends(get_current_user),db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user