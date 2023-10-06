#!/bin/sh
# Add your startup script
random_text=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)
echo "$random_text" > /home/ctf/canary.txt
cd home/ctf
exec 2>/dev/null
/usr/sbin/chroot --userspec=1000:1000 /home/ctf  ./I_want_2_LEAVE
# DO NOT DELETE
/etc/init.d/xinetd start;
sleep infinity;
