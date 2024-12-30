from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.customer import CustomerCreate, Customer, CustomerOut
from services.customer_service import CustomerService

router = APIRouter()

# Route pour créer un client
@router.post("/", response_model=Customer)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    created_customer = CustomerService.create_customer(db=db, customer=customer)
    return Customer.from_orm(created_customer)

# Route pour lister tous les clients
@router.get("/list", response_model=list[CustomerOut])
def list_customers(db: Session = Depends(get_db)):
    customers = CustomerService.get_customers(db=db)
    return [CustomerOut.from_orm(customer) for customer in customers]

# Route pour récupérer un client par ID
@router.get("/{customer_id}", response_model=CustomerOut)
def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    customer = CustomerService.get_customer_by_id(db=db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return CustomerOut.from_orm(customer)

# Route pour mettre à jour un client
@router.put("/{customer_id}", response_model=CustomerOut)
def update_customer(customer_id: int, customer: CustomerCreate, db: Session = Depends(get_db)):
    updated_customer = CustomerService.update_customer(db=db, customer_id=customer_id, customer=customer)
    if updated_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return CustomerOut.from_orm(updated_customer)

# Route pour supprimer un client
@router.delete("/{customer_id}", response_model=CustomerOut)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    deleted_customer = CustomerService.delete_customer(db=db, customer_id=customer_id)
    if deleted_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return CustomerOut.from_orm(deleted_customer)
