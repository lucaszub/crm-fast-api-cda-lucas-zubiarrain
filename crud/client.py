from sqlalchemy.orm import Session
from models.client import ClientDB

def create_client(db: Session, prenom: str, nom: str, numero:str= None, adress:str=None):
    client = ClientDB(prenom=prenom, nom=nom, numero=numero,adress=adress )
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

def get_client_by_id(db: Session, client_id: int):
    return db.query(ClientDB).filter(ClientDB.id == client_id).first()

def get_all_clients(db: Session):
    return db.query(ClientDB).all()


