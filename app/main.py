from fastapi import FastAPI
from .routers.health import router as health_router

app = FastAPI(title="FastAPI on Codespaces & Render")

@app.get("/")
def read_root():
    return {"message": "Hello from Codespaces + FastAPI + Render!"}
