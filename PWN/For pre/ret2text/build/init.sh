#!/bin/sh

echo "#!/bin/bash" > clear_task.sh
echo "find /tmp -type f -mmin +1 -delete" >> clear_task.sh
echo "* * * * * /home/pwn/clear_task.sh" > cron_job
crontab cron_job
chmod +x /home/pwn/clear_task.sh
/etc/init.d/cron start
service xinetd start && exec sleep infinity
