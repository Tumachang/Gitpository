from fastapi import FastAPI
from pydantic import BaseModel
import os
import sqlalchemy as sa

DATABASE_URL = os.environ.get("postgresql://pythonmember_user:4ufqkeLNv18yJzOFnZQoFKf0HxhxahJ2@dpg-d4j73oumcj7s73bbeaeg-a/pythonmember")  # 在 Render 上設定為 Internal URL
engine = sa.create_engine(DATABASE_URL, pool_pre_ping=True)

app = FastAPI()

class User(BaseModel):
    email: str
    password: str  # 實務上請改成雜湊後存

@app.get("/")
def health():
    # 簡單測試 DB 連線
    with engine.connect() as conn:
        conn.execute(sa.text("SELECT 1"))
    return {"status": "ok"}

@app.post("/signup")
def signup(user: User):
    # TODO: 以 SQLAlchemy ORM/Migrations 完成實務邏輯
    with engine.begin() as conn:
        conn.execute(sa.text(
            "INSERT INTO users(email, password) VALUES (:email, :password)"
        ), {"email": user.email, "password": user.password})
    return {"message": "created"}
