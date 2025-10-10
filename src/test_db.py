# src/test_db.py
from src.database import Base, engine
from src.models import User

def main():
    print("Conectando a la base y verificando tablas…")
    # Crea TODAS las tablas definidas en modelos que NO existan todavía
    Base.metadata.create_all(bind=engine)
    print("OK: tablas listas. (Si ya existían, no se tocaron)")

if __name__ == "__main__":
    main()
