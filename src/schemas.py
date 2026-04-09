from pydantic import BaseModel, EmailStr
#Validaciones con Pydantic

class UserCreate(BaseModel):
    """
    Esquema (modelo) que define qué datos
    esperamos recibir para crear un usuario.
    """
    name: str
    email: EmailStr  # valida formato de correo

class OrderCreate(BaseModel):
    product: str
    quantity: int
    price: int
    status: str = "pending"
    user_id: int

class OrderResponse(BaseModel):
    id: int
    product: str
    quantity: int
    price: int
    status: str
    user_id: int

class Config:
    orm_mode = True