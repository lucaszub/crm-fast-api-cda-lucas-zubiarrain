# models/appointment.py
from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.database import Base

class AppointmentDB(Base):
    __tablename__ = 'appointments'
    
    id_rdv = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(Date, nullable=False)
    heure = Column(Time, nullable=False)
    objet = Column(String, nullable=False)
    id_client = Column(Integer, ForeignKey('clients.id_client'), nullable=False)  # Clé étrangère

    # Définir la relation ici, après la définition complète de la classe
    client = relationship("ClientDB", back_populates="appointments")  # Relation inversée
