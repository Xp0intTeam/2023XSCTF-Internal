FROM ubuntu:22.04

RUN apt-get -y update --fix-missing
RUN apt-get -y upgrade
RUN apt-get -y install xinetd
RUN groupadd -r pwn && useradd -r -g pwn pwn

ADD build/pwn.xinetd /etc/xinetd.d/pwn
ADD build/init.sh /etc/init.sh
RUN chmod 700 /etc/init.sh
RUN chmod 1733 /tmp /var/tmp /dev/shm

WORKDIR /home/pwn
ADD qrun .
RUN chmod a+x qemu-system-riscv64 run.sh

RUN chown -R root:pwn /home/pwn
RUN chmod -R go-w /home/pwn
