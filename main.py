from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from schemas.client import ClientSchema
from services.client import ClientHandler
from db.database import Base, engine, get_db  # Import depuis database.py
from models.client import ClientDB
from rooters.client_router import router as client_router
from rooters.rendezvous_router import router as rdv_router

# === Créer les tables dans la base de données ===
Base.metadata.create_all(bind=engine)

# === Application FastAPI ===
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI!"}

app.include_router(client_router, prefix="/api", tags=["Clients"])
app.include_router(rdv_router, prefix="/api", tags=["rdv"])
