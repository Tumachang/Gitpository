from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI in Codespaces", version="0.1.0")

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/items")
def create_item(item: Item):
    return {"message": "item created", "item": item}

# 可直接在容器中用：python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
