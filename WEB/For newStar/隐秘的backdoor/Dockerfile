FROM vulhub/php:8.1-backdoor

COPY ./flag /flag
COPY ./index.php /var/www/html/index.php

RUN chmod 0755 /var/www/html/*
RUN chmod 755 /flag
RUN chown www-data:www-data /var/www/html/* -R
RUN chown root:root /flag

USER www-data