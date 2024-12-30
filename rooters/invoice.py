from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.invoice import InvoiceCreate, InvoiceOut
from services.invoice_service import InvoiceService

router = APIRouter()

@router.post("/", response_model=InvoiceOut)
def create_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    created_invoice = InvoiceService.create_invoice(db=db, invoice=invoice)
    return InvoiceOut.from_orm(created_invoice)

@router.get("/list", response_model=list[InvoiceOut])
def list_invoices(db: Session = Depends(get_db)):
    invoices = InvoiceService.get_invoices(db=db)
    return [InvoiceOut.from_orm(invoice) for invoice in invoices]

@router.get("/{invoice_id}", response_model=InvoiceOut)
def get_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = InvoiceService.get_invoice_by_id(db=db, invoice_id=invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return InvoiceOut.from_orm(invoice)

@router.put("/{invoice_id}", response_model=InvoiceOut)
def update_invoice(invoice_id: int, invoice: InvoiceCreate, db: Session = Depends(get_db)):
    updated_invoice = InvoiceService.update_invoice(db=db, invoice_id=invoice_id, invoice=invoice)
    if not updated_invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return InvoiceOut.from_orm(updated_invoice)

@router.delete("/{invoice_id}", response_model=InvoiceOut)
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    deleted_invoice = InvoiceService.delete_invoice(db=db, invoice_id=invoice_id)
    if not deleted_invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return InvoiceOut.from_orm(deleted_invoice)

@router.get("/invoices/{prenom}/{nom}")
def get_invoices_by_customer_name(prenom: str, nom: str, db: Session = Depends(get_db)):
    invoices = InvoiceService.get_invoices_by_customer_name(db, prenom, nom)
    if invoices:
        return invoices
    return {"message": "No invoices found for this customer."}