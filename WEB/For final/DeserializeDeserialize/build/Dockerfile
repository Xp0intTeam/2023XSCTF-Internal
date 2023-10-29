FROM openjdk:8u222-slim

COPY app /app
#COPY --chmod=500 init.sh /init.sh

WORKDIR /app
#RUN adduser -disabled-password -shell /bin/bash www-data
RUN useradd ctf\
  && echo "XSCTF{Y0u_4r3_a_deserialize_m4st3r!!}" > /flag

USER ctf

CMD ["java","-jar","/app/app.jar"]
