# src/dependencies.py

from src.database import SessionLocal

def get_db():
    """
    Esta función maneja una sesión de base de datos por cada request.
    FastAPI la usa automáticamente cuando la pedimos con Depends().
    """
    db = SessionLocal()  # abre una sesión nueva con la base (como abrir una conexión)
    try:
        yield db          # “cede” el control al endpoint que la use
    finally:
        db.close()        # al terminar la request, la sesión se cierra
