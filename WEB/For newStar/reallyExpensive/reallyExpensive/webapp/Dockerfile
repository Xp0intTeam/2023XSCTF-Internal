FROM openjdk:8-jdk-alpine
LABEL authors="justdoit"

WORKDIR /app
COPY app.jar /app/

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "/app/app.jar", "--spring.datasource.url=jdbc:mysql://myMysql:3306/db_buy_flag?characterEncoding=utf-8&serverTimezone=UTC"]
