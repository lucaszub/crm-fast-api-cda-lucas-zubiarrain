from sqlalchemy.orm import Session
from schemas.rendezvous import AppointmentSchema

class InvoiceService:
    def __init__(self, db: Session):
        self.db = db

    def generate_new_invoice(self, invoice: AppointmentSchema):
        """Générer une nouvelle facture."""
        pass

    def retrieve_invoice_by_id(self, invoice_id: int):
        """Récupérer une facture par ID."""
        pass

    def get_invoice_history_by_client(self, client_id: int):
        """Obtenir l'historique des factures d'un client."""
        pass

    def update_invoice_status(self, invoice_id: int, status: str):
        """Mettre à jour le statut d'une facture (payée, en attente, etc.)."""
        pass

    def send_invoice_reminder(self, invoice_id: int):
        """Envoyer un rappel de paiement pour une facture."""
        pass

    def calculate_total_invoice_amount(self, client_id: int):
        """Calculer le montant total des factures d'un client."""
        pass

    def archive_old_invoices(self, client_id: int):
        """Archiver les factures anciennes d'un client."""
        pass
