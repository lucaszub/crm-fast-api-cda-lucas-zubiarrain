# === Modèle Pydantic pour valider les données des requêtes ===
from pydantic import BaseModel
from typing import Optional, List


class ClientSchema(BaseModel):
    prenom: str
    nom: str
    numero: Optional[str] = None
    adress: Optional[str] = None

    # Utiliser from_attribute = True pour la conversion des objets SQLAlchemy en réponses JSON
    class Config:
        from_attribute = True