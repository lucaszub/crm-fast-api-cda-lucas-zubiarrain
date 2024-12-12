# 🚀 FastAPI CRM - Conteneurisation avec Docker

Ce guide vous explique comment construire et lancer votre application FastAPI avec Docker.

---

## 📦 Prérequis

- **Docker** doit être installé sur votre machine.  
  Vous pouvez le télécharger ici : [Docker - Get Started](https://www.docker.com/get-started).



## 🛠️ Construire l'image Docker

Pour construire l'image Docker de votre application FastAPI, utilisez la commande suivante :

```bash
docker build -t fastapi-crm:v1.0.6 .

```

Run l'image Docker

```bash
docker run -p 8000:8000 fastapi-crm:v1.0.6
```

Taguez votre image 
```bash
docker tag fastapi-crm:v1.0.6 lucaszub/fastapi-crm:v1.0.6

```
Pousser l'image vers Docker Hub (si vous voulez la partager ou l'utiliser ailleurs) :
```bash
docker login
docker push lucaszub/fastapi-crm:v1.0.6
```

ssh-keygen -t rsa -b 4096 -C "zubiarrainlucas@gmail.com"
