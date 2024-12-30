from pydantic import BaseModel, EmailStr, constr
from datetime import date
from typing import Optional

# Définir un type de chaîne de caractères avec une contrainte de regex pour le téléphone
# PhoneNumber = constr(regex=r'^\+?1?\d{9,15}$')

class CustomerCreate(BaseModel):
    nom: str
    prenom: str
    email: EmailStr  # Validation automatique de l'email
    phone: str  # Utilisation de PhoneNumber pour le téléphone
    address: str

class Customer(CustomerCreate):
    id_customer: int
    registration_date: date

    class Config:
        orm_mode = True

class CustomerOut(BaseModel):
    id_customer: int
    nom: str
    prenom: str
    email: str
    phone: str
    address: str
    registration_date: Optional[date]

    class Config:
        orm_mode = True
