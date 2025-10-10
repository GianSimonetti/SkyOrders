# src/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# 1 Cargar variables del .env
load_dotenv()

# 2 Armar la URL de conexión a PostgreSQL
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 3 Crear el motor de conexión (engine)
engine = create_engine(DATABASE_URL)

# 4 Crear el SessionLocal (maneja las sesiones con la BD)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5 Crear la base para declarar modelos (ORM)
Base = declarative_base()
