# models/client.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base


class ClientDB(Base):
    __tablename__ = 'clients'

    id_client = Column(Integer, primary_key=True, index=True, autoincrement=True)
    prenom = Column(String, nullable=False)
    nom = Column(String, nullable=False)
    numero = Column(String, nullable=True)
    adress = Column(String, nullable=True)

    # Définir la relation ici, après la définition complète de la classe
    appointments = relationship("AppointmentDB", back_populates="client")
