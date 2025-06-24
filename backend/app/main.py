from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title="ClinicFlow API")

@app.get("/")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}