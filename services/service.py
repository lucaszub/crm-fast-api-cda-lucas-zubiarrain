from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.service import ServiceCreate, ServiceOut
from models import Service

router = APIRouter()

class ServiceHandler:
    @staticmethod
    def create_service(db: Session, service:ServiceCreate):
        db_service = Service(
            service_name = service.service_name,
            description = service.description,
            price = service.price
        )
        db.add(db_service)
        db.commit()
        db.refresh(db_service)
        return db_service