from pydantic import BaseModel
from datetime import date
from typing import Optional

class InvoiceCreate(BaseModel):
    id_customer: int
    id_service: int
    amount: float
    issue_date: Optional[date] = None  # La date peut être optionnelle
    status: str

    class Config:
        orm_mode = True

class InvoiceOut(InvoiceCreate):
    id_invoice: int
    registration_date: Optional[date]

    class Config:
        orm_mode = True
