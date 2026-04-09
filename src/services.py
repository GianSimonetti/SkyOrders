from src.models import User
from fastapi import HTTPException
from src.models import Order
from src.models import User 

def get_users_service(db):
    return db.query(User).all()


def create_user_service(db, user):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    new_user = User(name=user.name, email=user.email)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def update_user_service(db, user_id, user):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db_user.name = user.name
    db_user.email = user.email

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user_service(db, user_id):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(db_user)
    db.commit()

    return {"message": "Usuario eliminado"}


def create_order_service(db, order):
    new_order = Order(
        product=order.product,
        quantity=order.quantity,
        price=order.price,
        status=order.status,
        user_id=order.user_id
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


def get_orders_service(db):
    return db.query(Order).all()