from fastapi import FastAPI
from rooters import customer  # Assure-toi que le chemin est correct (plutôt 'routers' que 'rooters')
from db.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# Crée l'instance FastAPI
app = FastAPI()
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



@app.get("/")
def hello_world():
    return {"message": "Hello, World"}  # Correction de la syntaxe de la réponse

# Inclure les routes du customer
app.include_router(customer.router)

# Créer les tables dans la base de données si elles n'existent pas encore
# Cela dépend de la façon dont tu gères ta base de données (migrations ou autre)
Base.metadata.create_all(bind=engine)

# Lancer l'application avec uvicorn:
# uvicorn main:app --reload # Pour le mode développement
