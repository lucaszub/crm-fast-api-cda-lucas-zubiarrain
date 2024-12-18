from sqlalchemy import Column, Integer, String, Float
from db.database import Base
from sqlalchemy.orm import relationship

class Service(Base):
    __tablename__ = "services"

    id_service = Column(Integer, primary_key=True, index=True)
    service_name = Column(String(100), index=True)  # Limite à 100 caractères pour le nom du service
    description = Column(String(255))  # Limite à 255 caractères pour la description du service
    price = Column(Float)

    invoices = relationship("Invoice", back_populates="service")
