
if [ "$USER" != 'amcmullin' ]
then

  echo "The Username is pi so we'll add a crontab"
  crontab -u pi -l > /tmp/crontab
  /bin/echo "* * * * * /usr/bin/sh /home/pi/Documents/EZ_Salt/HC-SR04/run.sh" >> /tmp/crontab
  crontab -u pi /tmp/crontab


#setup crontab here
#crontab syslog is in
  # I need to create a crontab first by [crontab -e]
  # crontab -u pi -l ; echo "* * * * * /usr/bin/sh /home/pi/Documents/EZ_Salt/HC-SR04/run.sh"
  #to remove
  #crontab -u pi -l | grep -v "* * * * * /usr/bin/sh /home/pi/Documents/EZ_Salt/HC-SR04/run.sh"

fi