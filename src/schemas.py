# src/schemas.py
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    """
    Esquema (modelo) que define qué datos
    esperamos recibir para crear un usuario.
    """
    name: str
    email: EmailStr  # valida formato de correo
