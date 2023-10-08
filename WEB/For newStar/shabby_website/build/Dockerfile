FROM node:lts-alpine3.15

COPY app /app
COPY init.sh /init.sh

WORKDIR /app
RUN adduser -D -G www-data -s /bin/ash www-data && \
    npm --registry https://registry.npmmirror.com/ install

CMD ["/init.sh"]
