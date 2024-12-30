from sqlalchemy.orm import Session
from models import Customer
from schemas.customer import CustomerCreate
import datetime

class CustomerService:
    @staticmethod
    def create_customer(db: Session, customer: CustomerCreate):
        db_customer = Customer(
            nom=customer.nom,
            prenom=customer.prenom,
            email=customer.email,
            phone=customer.phone,
            address=customer.address,
            registration_date=datetime.date.today()  # Date d'enregistrement par défaut
        )
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return db_customer

    @staticmethod
    def get_customers(db: Session):
        return db.query(Customer).all()
    
    @staticmethod
    def update_customer(db: Session, customer_id: int, customer: CustomerCreate):
        db_customer = db.query(Customer).filter(Customer.id_customer == customer_id).first()
        if db_customer:
            db_customer.nom = customer.nom
            db_customer.prenom = customer.prenom
            db_customer.email = customer.email
            db_customer.phone = customer.phone
            db_customer.address = customer.address
            db.commit()
            db.refresh(db_customer)
        return db_customer
    
    @staticmethod
    def delete_customer(db: Session, customer_id: int):
        db_customer = db.query(Customer).filter(Customer.id_customer == customer_id).first()
        if db_customer:
            db.delete(db_customer)
            db.commit()
            return db_customer
        return None

    @staticmethod
    def get_customer_by_id(db: Session, customer_id: int):
        return db.query(Customer).filter(Customer.id_customer == customer_id).first()
