FROM nimmis/apache-php5:latest

COPY index.php /var/www/html/index.php
RUN rm /var/www/html/index.html

CMD exec /bin/bash -c "/etc/init.d/apache2 start; trap : TERM INT; sleep infinity & wait"

EXPOSE 80 
