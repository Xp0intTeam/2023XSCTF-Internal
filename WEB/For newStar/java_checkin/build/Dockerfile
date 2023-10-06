FROM openjdk:17-slim

COPY app /app

WORKDIR /app
RUN useradd ctf\
    && echo "XSCTF{J@va_1s_v@3y_Imp03tAnt!!!!!!!!}" > /flag

USER ctf
CMD ["java", "-jar", "/app/checkin-0.0.1-SNAPSHOT.jar"]
