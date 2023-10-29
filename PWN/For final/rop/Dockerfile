FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i "s/archive.ubuntu.com/mirrors.ustc.edu.cn/g" /etc/apt/sources.list && \
    sed -i "s/security.ubuntu.com/mirrors.ustc.edu.cn/g" /etc/apt/sources.list && \
    apt-get update && apt-get -y dist-upgrade           && \
    apt-get install -y --no-install-recommends xinetd   && \
    apt-get clean && rm -rf /var/lib/apt/list/*

RUN useradd -m ctf                && \
    mkdir /home/ctf/usr           && \
    cp -R /lib* /home/ctf         && \
    cp -R /usr/lib* /home/ctf/usr && \
    mkdir /home/ctf/bin           && \
    cp /bin/sh /home/ctf/bin      && \
    cp /bin/ls /home/ctf/bin      && \
    cp /bin/cat /home/ctf/bin     && \
    mkdir /home/ctf/dev

WORKDIR /home/ctf/

COPY ./etc/start.sh   /
COPY ./etc/ctf.xinetd /etc/xinetd.d
COPY ./rop /home/ctf
COPY ./flag  /home/ctf

RUN chmod +x /start.sh          && \
    chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf      && \
    chmod 740 /home/ctf/flag

CMD exec /usr/bin/timeout 60 /usr/sbin/xinetd -dontfork -f /etc/xinetd.d/ctf.xinetd

EXPOSE 42002
