from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from db.database import Base
from sqlalchemy.sql import func

class Customer(Base):
    __tablename__ = "customers"

    id_customer = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    phone = Column(String(255))
    address = Column(String(255))
    registration_date = Column(Date, default=func.current_date())

    appointments = relationship("Appointment", back_populates="customer")
    invoices = relationship("Invoice", back_populates="customer")
    interactions = relationship("Interaction", back_populates="customer")
