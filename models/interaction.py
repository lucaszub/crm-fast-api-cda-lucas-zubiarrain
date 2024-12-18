from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db.database import Base
from sqlalchemy.orm import relationship

class Interaction(Base):
    __tablename__ = "interactions"

    id_interaction = Column(Integer, primary_key=True, index=True)
    id_customer = Column(Integer, ForeignKey("customers.id_customer"))
    interaction_date = Column(DateTime)  # Utilisation de DateTime pour gérer à la fois la date et l'heure
    description = Column(String(255))  # Limitation de la longueur du champ description à 255 caractères

    customer = relationship("Customer", back_populates="interactions")
