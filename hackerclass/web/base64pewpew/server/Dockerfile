FROM php:8.1-fpm-alpine

RUN apk update && apk add nginx 

COPY nginx.conf /etc/nginx/nginx.conf

COPY src /var/www/html

EXPOSE 80

# Start Nginx and PHP-FPM
CMD ["sh", "-c", "nginx && php-fpm"]
