from fastapi import FastAPI
from rooters import customer  # Assure-toi que le chemin est correct
from db.database import engine, Base

# Crée l'instance FastAPI
app = FastAPI()

# Inclure les routes du customer
app.include_router(customer.router)

# Créer les tables dans la base de données si elles n'existent pas encore
# Cela dépend de la façon dont tu gères ta base de données (migrations ou autre)
Base.metadata.create_all(bind=engine)

# Lancer l'application avec uvicorn:
# uvicorn main:app --reload
