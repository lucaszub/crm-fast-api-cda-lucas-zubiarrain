from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from schemas.client import ClientSchema
from services.client import ClientHandler
from db.database import get_db

router = APIRouter()

@router.get("/clients/test")
def test_hello():
    return {"hello: world"}


@router.post("/clients/")
def create_client(client:ClientSchema, db : Session = Depends(get_db)):
    service = ClientHandler(db)
    try:
        new_client = service.register_new_client(client)
        return {"message" : "Client ajouté avec succès", "client": new_client}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erreur lors de l'ajout du client")
    
@router.get("/clients/", response_model=List[ClientSchema])
def get_clients(db: Session = Depends(get_db)):
    service = ClientHandler(db)
    try:
        clients = service.get_all_clients()
        return clients
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erreur lors de la récupération des clients")