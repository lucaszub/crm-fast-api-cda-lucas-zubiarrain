from sqlalchemy import Column, Integer, ForeignKey, Float, Date, String
from db.database import Base
from sqlalchemy.orm import relationship

class Facture(Base):
    __tablename__ = "factures"

    id_facture = Column(Integer, primary_key=True, index=True)
    id_client = Column(Integer, ForeignKey("clients.id_client"))
    id_service = Column(Integer, ForeignKey("services.id_service"))
    montant = Column(Float)
    date_emission = Column(Date)
    statut = Column(String(50))  # Limité à 50 caractères pour le statut de la facture

    client = relationship("Client", back_populates="factures")
    service = relationship("Service", back_populates="factures")
