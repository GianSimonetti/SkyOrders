# src/models.py
from sqlalchemy import Column, Integer, String
from src.database import Base

# 1️⃣ Definimos la clase que representa la tabla "users"
class User(Base):
    __tablename__ = "users"  # nombre real de la tabla en PostgreSQL

    # 2️⃣ Definimos las columnas (campos)
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)

    # 3️⃣ Representación útil para depuración
    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
