from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.service import ServiceCreate, ServiceOut
from models import Service
from services.service import ServiceHandler
router = APIRouter()

@router.post("/service/", response_model=ServiceOut)
def create_service(service: ServiceCreate, db: Session = Depends(get_db)):
    created_service = ServiceHandler.create_service(db=db, service=service)
    return Service.from_orm(created_service) 


# @router.get("/customers/list", response_model=list[CustomerOut])
# def list_customers(db: Session = Depends(get_db)):
#     # Retourne tous les clients sans pagination
#     customers = CustomerService.get_customers(db=db)
#     return [CustomerOut.from_orm(customer) for customer in customers]
