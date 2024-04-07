FROM mysql:8.0.27
LABEL authors="justdoit"

ENV MYSQL_ROOT_PASSWORD 46d365e834c3462df0e6f14b66b2a761

ADD backup.sql /docker-entrypoint-initdb.d

EXPOSE 3306

