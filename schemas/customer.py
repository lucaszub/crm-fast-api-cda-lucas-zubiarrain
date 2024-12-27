from pydantic import BaseModel
from datetime import date
from typing import Optional
class CustomerCreate(BaseModel):
    nom: str
    prenom:str
    email: str
    phone: str
    address: str

class Customer(CustomerCreate):
    id_customer: int
    registration_date: date

    class Config:
        orm_mode = True

class CustomerOut(BaseModel):
    id_customer: int
    nom: str
    prenom:str
    email: str
    phone: str
    address: str
    registration_date: Optional[date]

    class Config:
        orm_mode = True