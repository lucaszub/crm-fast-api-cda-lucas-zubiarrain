from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.customer import CustomerCreate, Customer, CustomerOut  
from services.customer_service import CustomerService

router = APIRouter()

@router.post("/customers/", response_model=Customer)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return CustomerService.create_customer(db=db, customer=customer)

@router.get("/customers/list", response_model=list[CustomerOut])
def list_customers(db: Session = Depends(get_db)):
    # Retourne tous les clients sans pagination
    customers = CustomerService.get_customers(db=db)
    return [CustomerOut.model_validate(customer) for customer in customers]
