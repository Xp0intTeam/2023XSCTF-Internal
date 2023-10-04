FROM php:5.6-apache
ENV TimeZone=Asia/Shanghai
ARG user_id=1000
RUN usermod -u $user_id www-data; \
    ln -snf /usr/share/zoneinfo/$TimeZone /etc/localtime && echo $TimeZone > /etc/timezone; \
    chown -R www-data:www-data /var/www; \
    echo "ServerName localhost" >> /etc/apache2/apache2.conf
COPY init.sh /etc/init.sh
COPY www /var/www/html/

RUN chmod 500 /etc/init.sh;\
    mkdir /var/www/html/uploads;\
    chmod 777 /var/www/html/uploads

CMD /etc/init.sh && service apache2 restart && tail -F /var/log/apache2/access.log;
