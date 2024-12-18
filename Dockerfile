FROM python:3.9-buster

# Mettre à jour les dépôts et installer les dépendances système nécessaires
RUN apt-get update && \
    apt-get install -y --no-install-recommends libmariadb-dev gcc build-essential && \
    rm -rf /var/lib/apt/lists/*  # Nettoyer les fichiers temporaires

# Répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port sur lequel l'application tourne
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
