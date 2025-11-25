from fastapi import FastAPI

app = FastAPI(title="Codespaces FastAPI Example")

@app.get("/")
def read_root():
    return {"message": "Hello from Codespaces + FastAPI!"}

@app.get("/health")
def health():
    return {"status": "ok"}
