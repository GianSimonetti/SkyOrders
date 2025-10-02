from fastapi import FastAPI
import os
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

app = FastAPI(title="SkyOrders API")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "SkyOrders API running",
        "db_host": os.getenv("POSTGRES_HOST")
    }
