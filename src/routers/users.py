from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.schemas import UserCreate
from src.models import User
from src.services import (
    get_users_service,
    create_user_service,
    update_user_service,
    delete_user_service
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