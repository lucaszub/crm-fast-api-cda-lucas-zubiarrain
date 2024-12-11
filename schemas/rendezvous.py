from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime, date, time

class AppointmentSchema(BaseModel):
    date: str  # Changer en chaîne pour la validation
    heure: str  # Changer en chaîne pour la validation
    objet: str  # ID du client associé au rendez-vous
    nom: Optional[str] = None  # Nom du client (facultatif pour validation)
    prenom: Optional[str] = None  # Prénom du client (facultatif pour validation)

    # Utilisation de field_validator pour Pydantic v2
    @field_validator('date')
    def validate_date(cls, value):
        try:
            # Validation du format de la date
            return datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError('Invalid date format, should be YYYY-MM-DD')

    # Validator pour convertir la chaîne en heure
    @field_validator('heure')
    def validate_time(cls, value):
        try:
            # Validation du format de l'heure
            return datetime.strptime(value, '%H:%M').time()
        except ValueError:
            raise ValueError('Invalid time format, should be HH:MM')

    class Config:
        from_attribute = True  # Pour intégrer les modèles SQLAlchemy


class AppointmentUpdateSchema(BaseModel):
    date: Optional[str] = None  # Optionnel, pour mettre à jour la date
    heure: Optional[str] = None  # Optionnel
    objet: Optional[str] = None  # Optionnel

    # Validators similaires pour les mises à jour
    @field_validator('date')
    def validate_date(cls, value):
        if value:
            try:
                return datetime.strptime(value, '%Y-%m-%d').date()
            except ValueError:
                raise ValueError('Invalid date format, should be YYYY-MM-DD')
        return value

    @field_validator('heure')
    def validate_time(cls, value):
        if value:
            try:
                return datetime.strptime(value, '%H:%M').time()
            except ValueError:
                raise ValueError('Invalid time format, should be HH:MM')
        return value

    class Config:
        from_attribute = True  # Permet de mapper avec les modèles SQLAlchemy


class AppointmentResponseSchema(BaseModel):
    date: date
    heure: time
    objet: str
    nom_client: str
    prenom_client: str

    class Config:
        from_attribute = True
