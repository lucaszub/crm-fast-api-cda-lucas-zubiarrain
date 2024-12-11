from crud.client import create_client, get_client_by_id, get_all_clients
from sqlalchemy.orm import Session
from schemas.client import ClientSchema

class ClientHandler:
    def __init__(self, db: Session):
        self.db = db

    def register_new_client(self, client: ClientSchema):
        """Méthode pour enregistrer un nouveau client."""
        if not client.prenom or not client.nom:
            raise ValueError("Le prénom et le nom sont obligatoires")
        new_client = create_client(self.db, client.prenom, client.nom, client.numero, client.adress)
        return new_client

    def retrieve_client_by_id(self, client_id: int):
        """Méthode pour récupérer un client par ID."""
        client = get_client_by_id(self.db, client_id)
        if not client:
            raise ValueError("Client non trouvé")
        return client

    def get_all_clients(self):
        """Méthode pour récupérer tous les clients."""
        return get_all_clients(self.db)

    def delete_client_by_id(self, client_id: int):
        """Méthode pour supprimer un client par ID."""
        pass

    def update_client_details(self, client_id: int, client_data: ClientSchema):
        """Méthode pour mettre à jour les informations d'un client."""
        pass

    def search_clients_by_name(self, search_term: str):
        """Rechercher des clients par nom ou prénom."""
        pass

    def list_clients_with_recent_activity(self):
        """Lister les clients avec une activité récente (rendez-vous, factures, etc.)."""
        pass

    def send_marketing_email(self, client_id: int):
        """Envoyer un email marketing à un client."""
        pass

    def calculate_client_lifetime_value(self, client_id: int):
        """Calculer la valeur à vie d'un client (CLV)."""
        pass

    def tag_client_as_vip(self, client_id: int):
        """Marquer un client comme VIP pour un traitement prioritaire."""
        pass

    def archive_inactive_clients(self):
        """Archiver les clients inactifs depuis une période donnée."""
        pass
