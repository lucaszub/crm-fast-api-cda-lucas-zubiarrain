from sqlalchemy import Column, Integer, String, ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "tasks"

    id_task = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)  # Limité à 255 caractères pour le titre
    description = Column(String(1000))  # Limité à 1000 caractères pour la description (modifiable selon l'usage)
    id_user = Column(Integer, ForeignKey("users.id_user"))
    due_date = Column(String(50))  # Limité à 50 caractères pour la date (format d'une chaîne de caractères, ou utiliser Date)

    user = relationship("User", back_populates="task")  # Changement ici
