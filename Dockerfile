# Utilise une image officielle de Python comme base
FROM python:3.9-alpine

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installe les dépendances test
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le contenu de l'application dans le conteneur
COPY . .

# Expose le port sur lequel l'application va écouter test
EXPOSE 8000

# Commande pour lancer l'application avec uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
