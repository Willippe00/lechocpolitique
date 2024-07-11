#!/bin/bash

# Variables pour les fichiers de certificat et de clé
certfile=/home/william/Documents/production/lechocpolitique/SSL/certfile.pem
keyfile=/home/william/Documents/production/lechocpolitique/SSL/keyfile.pem

# Commande pour lancer gunicorn avec SSL/TLS
# Assurez-vous d'utiliser le chemin correct pour le module wsgi
gunicorn --workers 4 --bind 0.0.0.0:5000 --certfile=$certfile --keyfile=$keyfile mainProd:app
