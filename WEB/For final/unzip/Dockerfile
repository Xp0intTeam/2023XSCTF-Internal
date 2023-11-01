FROM node:latest
WORKDIR /app
COPY app .
COPY start.sh /
COPY flag /
RUN chmod a+x /start.sh
ENTRYPOINT ["bash", "/start.sh"]

