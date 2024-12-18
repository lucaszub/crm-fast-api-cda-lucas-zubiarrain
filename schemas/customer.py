from pydantic import BaseModel
from datetime import date
from typing import Optional
class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class Customer(CustomerCreate):
    id_customer: int
    registration_date: date

    class Config:
        from_attributes = True

class CustomerOut(BaseModel):
    id_customer: int
    name: str
    email: str
    phone: str
    address: str
    registration_date: Optional[date]

    class Config:
        from_attributes = True