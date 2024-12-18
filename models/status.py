from sqlalchemy import Column, Integer, String
from db.database import Base

class Status(Base):
    __tablename__ = "statuses"

    id_status = Column(Integer, primary_key=True, index=True)
    status_name = Column(String(50), index=True)  # Limite à 50 caractères pour le nom du statut
