from fastapi import FastAPI
from rooters import customer, service, appointment  # Assure-toi que le chemin vers 'appointment' est correct
from db.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# Crée l'instance FastAPI
app = FastAPI(
    title="Coaching Application API",
    description="API pour la gestion des rendez-vous, clients et autres aspects de l'application pour les coachs sportifs.",
    version="1.0.0"
)

# Liste des origines autorisées
origins = [
    "http://localhost:3000",  # Frontend en développement
    "https://lzubdev.com",
    "http://localhost:5174",
    "http://localhost:5173"
    # Ajoute d'autres origines si nécessaire
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Autoriser les origines spécifiées
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autoriser tous les en-têtes
)

@app.get("/", tags=["General"])
def hello_world():
    """
    Endpoint pour tester la connexion à l'API.
    Retourne un message 'Hello, World'.
    """
    return {"message": "Hello, World"}

# Inclure les routes du customer, service et appointment
app.include_router(customer.router, prefix="/customers", tags=["Customers"])
app.include_router(service.router, prefix="/services", tags=["Services"])
app.include_router(appointment.router, prefix="/appointments", tags=["Appointments"])

# Créer les tables dans la base de données si elles n'existent pas encore
Base.metadata.create_all(bind=engine)
