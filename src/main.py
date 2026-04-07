from fastapi import FastAPI
from src.routers import users

app = FastAPI(title="SkyOrders API")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "SkyOrders API running"
    }

app.include_router(users.router)