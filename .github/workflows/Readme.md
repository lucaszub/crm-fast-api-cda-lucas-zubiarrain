# Documentation : Nom de Domaine, Certificat SSL Let's Encrypt, et NGINX

## Sommaire

- **Configuration du Nom de Domaine**

- **Installation et Configuration de NGINX**

- **Mise en Place du Certificat SSL Let's Encrypt**

- **Automatisation du Renouvellement**

- **Dépannage Courant**

## Configuration du Nom de Domaine

### Choix du nom de domaine :

- Utilisation de "**lzubdev.com**" comme nom de domaine principal.

### Achat et gestion :

- Le nom de domaine a été acheté via un régistraire comme hostinger dans mon cas

### Configuration DNS :

Ajout des enregistrements DNS pour pointer vers le 

- serveur (IP publique) :

- A Record : @ -> 123.45.67.89

- CNAME Record : www -> @

**Exemple de configuration DNS :**

| Type  | Name | Value        | TTL  |
|-------|------|--------------|------|
| A     | @    | 123.45.67.89 | 3600 |
| CNAME | www  | @            | 3600 |


## Installation et Configuration de NGINX

### Installation de NGINX sur un serveur Ubuntu :
```bash
sudo apt update
sudo apt install nginx
```

### Démarrer et activer NGINX :
```bash
sudo systemctl start nginx
sudo systemctl enable nginx
```

### Configuration du Virtual Host :

**Création d'un fichier de configuration pour le site :**

```bash
sudo nano /etc/nginx/sites-available/lzubdev.com
```

Exemple de contenu :

```bash
server {
    listen 80;
    server_name lzubdev.com www.lzubdev.com;

    root /var/www/lzubdev.com/html;
    index index.html index.htm;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### Activer le site et tester NGINX :
```bash
sudo ln -s /etc/nginx/sites-available/lzubdev.io /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```
## Mise en Place du Certificat SSL Let's Encrypt

## Installation de Certbot :
```bash
sudo apt install certbot python3-certbot-nginx
```
### Obtenir le certificat SSL :
```bash
sudo certbot --nginx -d lzubdev.com -d www.lzubdev.com
```

## Suivre les instructions pour vérifier le domaine et installer le certificat.

### Certbot modifie automatiquement la configuration NGINX pour inclure le SSL.

**Exemple de configuration SSL modifiée :**
```bash
server {
    listen 443 ssl;
    server_name lzubdev.com www.lzubdev.com;

    ssl_certificate /etc/letsencrypt/live/lzubdev.col/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/lzubdev.com/privkey.pem;

    root /var/www/lzubdev.io/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}


server {
    listen 80;
    server_name lzubdev.io www.lzubdev.io;
    return 301 https://$host$request_uri;
}
```

## Automatisation du Renouvellement

Certbot renouvelle automatiquement les certificats. Pour vérifier le renouvellement automatique :
```bash
sudo systemctl status certbot.timer
```

### Simulation du renouvellement manuel :
```bash
sudo certbot renew --dry-run
```

**Dépannage Courant** :

- Erreur de vérification DNS lors du certificat SSL :

- Vérifier que les enregistrements DNS sont correctement configurés et propagés.

- Utiliser https://dnschecker.org pour tester.

NGINX ne redémarre pas :
```bash
sudo nginx -t
sudo systemctl restart nginx
```

**Forcer le renouvellement du certificat SSL :**
```bash
sudo certbot renew --force-renewal
```

Références et Tutoriels Utilisés

Documentation Officielle de NGINX

Certbot - Let's Encrypt

Tutoriel DigitalOcean : Configuration NGINX et SSL