from sqlalchemy.orm import Session
from models.appointment import AppointmentDB
from schemas.rendezvous import AppointmentSchema, AppointmentUpdateSchema, AppointmentResponseSchema
from models.client import ClientDB
from datetime import date

def create_appointment(db: Session, appointment_data: AppointmentSchema):
    # Vérifie si un client correspondant au nom/prénom existe
    client = db.query(ClientDB).filter(
        ClientDB.nom == appointment_data.nom,
        ClientDB.prenom == appointment_data.prenom
    ).first()

    if not client:
        raise ValueError("Le client avec ce nom et prénom n'existe pas.")

    # Crée un rendez-vous lié au client trouvé
    new_appointment = AppointmentDB(
        date=appointment_data.date,
        heure=appointment_data.heure,
        objet=appointment_data.objet,
        id_client=client.id_client  # Associe le rendez-vous au client
    )

    # Ajoute et commite les données dans la base de données
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)  # Recharge l'objet pour obtenir l'ID généré

    return new_appointment


def find_appointments_by_customer_name(db: Session, nom: str, prenom: str):
    """
    Cette fonction récupère tous les rendez-vous d'un client donné par son nom et prénom.
    """
    # Rechercher le client par nom et prénom
    client = db.query(ClientDB).filter(ClientDB.nom == nom, ClientDB.prenom == prenom).first()

    # Si aucun client n'est trouvé
    if not client:
        raise ValueError(f"Aucun client trouvé avec le nom {nom} et prénom {prenom}")

    # Récupérer les rendez-vous du client
    appointments = client.appointments

    # Si le client n'a pas de rendez-vous
    if not appointments:
        return {"message": "Pas de rendez-vous pour ce client."}

    # Créer une liste avec les rendez-vous
    client_appointments = []
    for appointment in appointments:
        client_appointments.append({
            'date': appointment.date,
            'heure': appointment.heure,
            'objet': appointment.objet
        })

    return client_appointments


def update_appointment_by_client_and_date(db: Session, nom: str, prenom: str, date: date, update_data: AppointmentUpdateSchema):
    """
    Met à jour les informations d'un rendez-vous en utilisant le nom, prénom et la date comme critères.
    """
    # Recherche du client
    client = db.query(ClientDB).filter(ClientDB.nom == nom, ClientDB.prenom == prenom).first()

    if not client:
        raise ValueError(f"Aucun client trouvé avec le nom {nom} et prénom {prenom}")

    # Recherche du rendez-vous
    appointment = db.query(AppointmentDB).filter(
        AppointmentDB.id_client == client.id_client,
        AppointmentDB.date == date
    ).first()

    if not appointment:
        raise ValueError(f"Aucun rendez-vous trouvé pour {nom} {prenom} à la date {date}")

    # Mise à jour des informations du rendez-vous
    if update_data.date:
        appointment.date = update_data.date
    if update_data.heure:
        appointment.heure = update_data.heure
    if update_data.objet:
        appointment.objet = update_data.objet

    # Enregistrer les modifications dans la base de données
    db.commit()
    db.refresh(appointment)

    # Renvoi d'un schéma de réponse structuré
    return AppointmentResponseSchema.from_orm(appointment)
