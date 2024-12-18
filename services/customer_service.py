from sqlalchemy.orm import Session
from models import Customer
from schemas.customer import CustomerCreate

class CustomerService:
    @staticmethod
    def create_customer(db: Session, customer: CustomerCreate):
        db_customer = Customer(
            name=customer.name,
            email=customer.email,
            phone=customer.phone,
            address=customer.address
        )
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return db_customer

    @staticmethod
    def get_customers(db: Session):
        return db.query(Customer).all()
    
    