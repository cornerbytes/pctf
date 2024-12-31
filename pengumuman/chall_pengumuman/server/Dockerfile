FROM php:8.1-fpm-alpine

RUN apk update && apk add nginx 

COPY nginx.conf /etc/nginx/nginx.conf

COPY src /var/www/html

COPY announcement.txt /announcement.txt

EXPOSE 80

RUN chown -R www-data:www-data /var/lib/nginx
# Start Nginx and PHP-FPM
CMD ["sh", "-c", "nginx && php-fpm"]
