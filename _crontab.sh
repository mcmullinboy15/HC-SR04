
if [ "$USER" != 'amcmullin' ]
then

  if grep "\* \* \* \* \* /usr/bin/sh /home/pi/Documents/EZ_Salt/HC-SR04/run.sh" /tmp/crontab    #"\*\/5 \* \* \* \* /usr/local/bin/test.sh" /var/spool/cron/root
  then
    echo "\033[34m  Entry already in crontab  \033[0m"
  else
#    echo "*/5 * * * * /usr/local/bin/test.sh" >>  /var/spool/cron/root


    echo "\033[34m  The Username is pi so we'll add a crontab  \033[0m"
    crontab -u pi -l > /tmp/crontab
    /bin/echo "* * * * * /usr/bin/sh /home/pi/Documents/EZ_Salt/HC-SR04/run.sh" >> /tmp/crontab
    crontab -u pi /tmp/crontab

  fi

#setup crontab here
#crontab syslog is in
  # I need to create a crontab first by [crontab -e]
  # crontab -u pi -l ; echo "* * * * * /usr/bin/sh /home/pi/Documents/EZ_Salt/HC-SR04/run.sh"
  #to remove
  #crontab -u pi -l | grep -v "* * * * * /usr/bin/sh /home/pi/Documents/EZ_Salt/HC-SR04/run.sh"

fi