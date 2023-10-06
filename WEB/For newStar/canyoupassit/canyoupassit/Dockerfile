FROM php:8.1-apache
LABEL author="justdoit"

RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

COPY index.php /var/www/html/index.php
COPY flag /flag
CMD ["/bin/sh", "-c", "php -S 0.0.0.0:80 2> /dev/null"]