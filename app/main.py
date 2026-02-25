from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

TOKEN = "supertoken123"

class Client(BaseModel):
    name: str
    age: int
    income: float
    country: str

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/score")
def score(client: Client, authorization: Optional[str] = Header(None)):
    if authorization != f"Bearer {TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    if client.age < 18:
        raise HTTPException(status_code=400, detail="Client must be adult")

    score = 0
    if client.age > 25:
        score += 30
    if client.income > 1000:
        score += 40
    if client.income > 3000:
        score += 30

    return {
        "name": client.name,
        "score": score,
        "risk_level": "LOW" if score >= 70 else "MEDIUM" if score >= 40 else "HIGH"
    }
