FROM ghcr.io/w4terdr0p/w4terctf-2023/gmpy2:alpine

COPY --chmod=777 chall.py  /home/ctf
COPY --chown=ctf:ctf flag1  /flag1
COPY --chown=ctf:ctf flag2 /flag2
COPY xinetd.conf /etc/xinetd.conf
COPY --chmod=777 key.pem /home/ctf/key.pem
COPY --chmod=500 init.sh /init.sh

CMD ["/init.sh"]
