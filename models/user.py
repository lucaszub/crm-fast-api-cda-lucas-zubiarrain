from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # 255 caractères pour le nom
    email = Column(String(255), unique=True, index=True)  # 255 caractères pour l'email
    password = Column(String(255))  # 255 caractères pour le mot de passe
    date_created = Column(Date)
    date_updated = Column(Date)
    id_role = Column(Integer, ForeignKey("roles.id_role"))  # Correction ici

    appointments = relationship("Appointment", back_populates="user")
    role = relationship("Role", back_populates="users")
    task = relationship("Task", back_populates="user")  # Pas de changement ici
