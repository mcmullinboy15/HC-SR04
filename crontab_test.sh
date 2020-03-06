#!/bin/bash

# Most Help
# https://www.golinuxcloud.com/create-schedule-cron-job-shell-script-linux/

CRON_FILE="/var/spool/cron/crontabs"

chmod u=rwx,g=wx,o=t $CRON_FILE

sudo touch $CRON_FILE
sudo /usr/bin/crontab $CRON_FILE
sudo echo "* * * * * /usr/bin/sh /home/pi/Documents/EZ_Salt/HC-SR04/run.sh" >> $CRON_FILE
sudo crontab -u pi -l

