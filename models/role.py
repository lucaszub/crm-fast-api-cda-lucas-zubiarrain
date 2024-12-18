from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class Role(Base):
    __tablename__ = "roles"

    id_role = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(255), index=True)

    users = relationship("User", back_populates="role")  # Ajout de la relation
