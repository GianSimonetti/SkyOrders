# src/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

from src.dependencies import get_db
from src.models import User
from src.schemas import UserCreate  # ← importamos el esquema nuevo

# Carga las variables del archivo .env
load_dotenv()

app = FastAPI(title="SkyOrders API")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "SkyOrders API running",
        "db_host": os.getenv("POSTGRES_HOST")
    }

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    """
    Endpoint que devuelve todos los usuarios desde la base de datos.
    """
    users = db.query(User).all()  # traduce a: SELECT * FROM users;
    return [{"id": u.id, "name": u.name, "email": u.email} for u in users]

@app.post("/users", status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo usuario en la base de datos.
    """
    # Verificar si ya existe el email (por restricción UNIQUE)
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    # Crear un nuevo objeto User (modelo ORM)
    new_user = User(name=user.name, email=user.email)

    # Agregarlo a la sesión y confirmar los cambios
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # refresca con datos reales de la DB (id autogenerado)

    # Devolver el usuario creado (en formato JSON)
    return {"id": new_user.id, "name": new_user.name, "email": new_user.email}