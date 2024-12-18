from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from db.database import Base
from sqlalchemy.orm import relationship

class Appointment(Base):
    __tablename__ = "appointments"

    id_appointment = Column(Integer, primary_key=True, index=True)
    id_customer = Column(Integer, ForeignKey("customers.id_customer"))
    id_user = Column(Integer, ForeignKey("users.id_user"))
    date_time = Column(DateTime)
    description = Column(String(255))  # Ajout de la longueur de 255 caractères pour la description

    customer = relationship("Customer", back_populates="appointments")
    user = relationship("User", back_populates="appointments")
