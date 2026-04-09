from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

##Tablas en bd

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    status = Column(String, default="pending")

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", backref="orders")