# Dockerfile pour Nginx
FROM nginx:latest

COPY default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /var/www/certbot

CMD ["nginx", "-g", "daemon off;"]
