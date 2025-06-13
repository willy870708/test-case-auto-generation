# main.py
from fastapi import FastAPI
from api.v1.routers import test_generator

app = FastAPI(
    title="AI TestGen Assistant API (Python 3.8)",
    version="1.0.0"
)

app.include_router(test_generator.router, prefix="/api/v1", tags=["Test Generation"])

@app.get("/")
def read_root():
    return {"message": "Welcome to AI TestGen Assistant API (Python 3.8)"}