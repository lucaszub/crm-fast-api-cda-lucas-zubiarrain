from sqlalchemy.orm import Session
from models import Invoice, Customer
from schemas.invoice import InvoiceCreate, InvoiceOut
from datetime import date

class InvoiceService:
    @staticmethod
    def create_invoice(db: Session, invoice: InvoiceCreate):
        db_invoice = Invoice(
            id_customer=invoice.id_customer,
            id_service=invoice.id_service,
            amount=invoice.amount,
            issue_date=invoice.issue_date or date.today(),  # Si aucune date fournie, prendre la date actuelle
            status=invoice.status
        )
        db.add(db_invoice)
        db.commit()
        db.refresh(db_invoice)
        return db_invoice

    @staticmethod
    def get_invoices(db: Session):
        return db.query(Invoice).all()

    @staticmethod
    def get_invoice_by_id(db: Session, invoice_id: int):
        return db.query(Invoice).filter(Invoice.id_invoice == invoice_id).first()

    @staticmethod
    def update_invoice(db: Session, invoice_id: int, invoice: InvoiceCreate):
        db_invoice = db.query(Invoice).filter(Invoice.id_invoice == invoice_id).first()
        if db_invoice:
            db_invoice.id_customer = invoice.id_customer
            db_invoice.id_service = invoice.id_service
            db_invoice.amount = invoice.amount
            db_invoice.issue_date = invoice.issue_date or date.today()  # Mise à jour de la date si nécessaire
            db_invoice.status = invoice.status
            db.commit()
            db.refresh(db_invoice)
        return db_invoice

    @staticmethod
    def delete_invoice(db: Session, invoice_id: int):
        db_invoice = db.query(Invoice).filter(Invoice.id_invoice == invoice_id).first()
        if db_invoice:
            db.delete(db_invoice)
            db.commit()
            return db_invoice
        return None
    
    @staticmethod
    def get_invoices_by_customer_name(db: Session, prenom: str, nom: str):
        # Recherche les factures liées à un client par son prénom et nom
        return db.query(Invoice).join(Customer).filter(Customer.prenom == prenom, Customer.nom == nom).all()
