# Backend - Outil de Gestion pour Petites Entreprises (en cours)  

## **Présentation**  
Ce backend est développé avec **FastAPI** pour répondre aux besoins des petites entreprises. Il gère les fonctionnalités principales de l'application, notamment :  
- **Gestion des clients** : Création, modification, suppression et recherche.  
- **Prise de rendez-vous** : Planification via un calendrier (en cours de développement).  
- **Rapports** : Génération et export des données en formats CSV et PDF (en cours).  

Le backend est conteneurisé avec **Docker** et utilise une base de données **MySQL**.  

---

## **Technologies Utilisées**  
- **FastAPI** : Framework rapide et moderne pour les APIs en Python.  
- **MySQL** : Base de données relationnelle utilisée pour stocker les données.  
- **Docker** : Utilisé pour packager et déployer l’application facilement.  
- **Nginx** : Proxy inverse pour gérer les requêtes HTTP et HTTPS.  

---

## **Infrastructure Actuelle**  
- **Base de données** : MySQL (hébergée en conteneur Docker).  
- **CI/CD** : GitHub Actions configuré pour :  
  - Construire et pousser les images Docker vers Docker Hub.  
  - Déployer automatiquement les nouvelles versions sur un VPS.  
- **Hébergement** :  
  - VPS avec un certificat HTTPS configuré via **Nginx**.  
  - Nom de domaine personnalisé pour accéder à l’API.  

---

## **Endpoints Principaux**  
- **Clients** :  
  - `POST /clients` : Ajouter un client.  
  - `GET /clients` : Récupérer la liste des clients.  
  - `GET /clients/{id}` : Détails d’un client.  
  - `PUT /clients/{id}` : Modifier un client.  
  - `DELETE /clients/{id}` : Supprimer un client.  

- **Rendez-vous** (en cours de développement) :  
  - `POST /rendezvous` : Ajouter un rendez-vous.  
  - `GET /rendezvous` : Récupérer les rendez-vous.  

La documentation complète des endpoints est disponible sur :  
- **Swagger** : `/docs`  
- **ReDoc** : `/redoc`  

---

## **Prochaines Améliorations**  
- Renforcement de la sécurité (gestion des accès et des secrets).  
- Implémentation d’un système de permissions avancé.  
- Ajout de tests unitaires et d’intégration.  
- Migration progressive vers un cloud (Azure).  
