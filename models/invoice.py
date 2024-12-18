from sqlalchemy import Column, Integer, ForeignKey, Float, Date, String
from db.database import Base
from sqlalchemy.orm import relationship

class Invoice(Base):
    __tablename__ = "invoices"

    id_invoice = Column(Integer, primary_key=True, index=True)
    id_customer = Column(Integer, ForeignKey("customers.id_customer"))
    id_service = Column(Integer, ForeignKey("services.id_service"))
    amount = Column(Float)
    issue_date = Column(Date)
    status = Column(String(50))  # Définir une longueur raisonnable pour le champ status

    customer = relationship("Customer", back_populates="invoices")
    service = relationship("Service", back_populates="invoices")
