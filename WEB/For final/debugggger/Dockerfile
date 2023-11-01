FROM python:3-slim-stretch

WORKDIR /app

RUN pip install flask
COPY ./src /app/
COPY ./run.sh /run.sh
COPY ./Fffff111114444gggggg /Fffff111114444gggggg

RUN useradd --create-home --no-log-init --shell /bin/bash xsctf \
&& adduser xsctf  users\
&& echo 'xsctf:123456' | chpasswd

RUN chmod 0755 /app/*
RUN chown xsctf:xsctf /app/* -R
RUN chmod 755 /Fffff111114444gggggg
RUN chown root:root /Fffff111114444gggggg
#RUN useradd hsctf && echo "hsctf hard nproc 10" >> /etc/security/limits.conf && chmod +x /run.sh
RUN chmod +x /run.sh
USER xsctf
CMD [ "/run.sh" ]
