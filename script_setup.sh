#!/bin/sh

# rpi.gpio
# right before not importing pandas

desired_python_version="Python 3.7"

SECONDS=0

if [ "$(. is_setup_complete.sh)" = 'true' ]
then
  echo "\033[34m  Skipping Setup because its Already Done  \033[0m"
else
  echo "\033[34m  updating raspberry pi  \033[0m"

  echo "\033[34m  full-upgrade  \033[0m"
  echo 'q' | sudo apt -y full-upgrade #1+ hour
  echo "\033[34m  apt-get update  \033[0m"
  sudo apt-get update
  echo "\033[34m  apt-get upgrade  \033[0m"
#  echo "" |      # It said the desktop might hvae changed press ok
  sudo apt-get -y upgrade --fix-missing


  echo "\033[34m  Enableing ssh server  \033[0m"
  sudo systemctl enable ssh

  echo "\033[34m  starting something??  maybe ssh  \033[0m"
  sudo systemctl start ssh

# hostname -I # to get IP-Address

# Here I set up a server. So as long as I have the IP address I can access it locally
  #sudo apt install apache2 -y
# move to 'pi' user and edit the index.html file
  #cd /var/www/html
  #sudo chown pi: index.html
# In oder for tapache to understand PHP
  #sudo apt install php libapache2-mod-php -y
  #sudo leafpad index.php
  #add this <?php header( 'Location: /index.html' ) ;  ?>

  # Here I set up a non-local server to acces it anywhere
  #sudo apt update && sudo apt install -y connectd && sudo connectd_installer
  # echo 1
  # echo 'ezsalt.dev.env@gmail.com'
  # echo 'ezsalt98'


  if [[ "$( python3 --version )" =~ $desired_python_version ]]
  then
    echo "\033[34m  PYTHON Already exists  \033[0m"
  else
    echo "\033[34m  upgrading python  \033[0m"
    sudo apt-get install
    . python_update.sh
  fi

  sleep 10

  path="$HOME/Documents/EZ_Salt/HC-SR04"
  if [ -d "$path" ]
  then
    echo "\033[34m  Directory $path exists.  \033[0m"
    cd "$HOME"/Documents/EZ_Salt/HC-SR04/ || return

  else
    echo "\033[34m  creating path to repo  \033[0m"
    mkdir -p "$HOME"/Documents/EZ_Salt
    cd "$HOME"/Documents/EZ_Salt/ || return

    echo "\033[34m  cloning the git repo from ezsaltdevenv/HC-SR04.git  \033[0m"
    git clone https://ezsaltdevenv:ezsalt98@github.com/ezsaltdevenv/HC-SR04.git

    echo "\033[34m  entering git repo  \033[0m"
    cd "$HOME"/Documents/EZ_Salt/HC-SR04/ || return
  fi

  sleep 10

  # What if I got this data off the Database
  echo 'setup_complete,email,name,phone_number,username,password,home_address,WIFI_username,WIFI_password,size_of_container,single_noti_1,single_noti_2,single_noti_3,daily_noti,send_daily,time_of_day
-1,"ezsalt.dev.env@gmail.com","Andrew","8018973786","ezsalt","ezsalt98","3869 w 9380 s, West Jordan, Ut 84088","oldfarm-5G","OldFarmpa$$",121.5,50,30,-1,15,TRUE,8'

  sleep 3

  if ping -q -c 1 -W 1 google.com >/dev/null; then
    echo "\033[34m  The network is up  \033[0m"
  else
    echo "\033[34m  setting up user wifi  \033[0m"
    python3 wifi_setup.py
  fi


  sleep 20


  echo "\033[34m  changing terminal design temporarily  \033[0m"
  #chsh -s /bin/bash
  #'This has the pi@raspberry tag'    export PS1='\[\033[32m\]\[\033[m\]@\[\033[32m\] \[\033[33;1m\]\w\[\033[m\] (\$(git branch 2>/dev/null | grep '^*' | colrm 1 2)) $ '
  #'This has the time as the tag'
  export PS1='\[\033[0;32m\]\[\033[0m\033[0;32m\][\@]\[\033[0;33m\]\w\[\033[0;36m\]$(__git_ps1)\n\[\033[0;32m\]\[\033[0m\033[0;32m\]\$\[\033[0m\033[0;32m\]\[\033[0m\] '

  echo "\033[34m  installing the nesseccary libraries  \033[0m"
  echo "\033[34m  sudo apt-get -y install rpi.gpio  \033[0m"
  sudo apt-get -y install rpi.gpio
  pip install -y RPi.GPIO
  echo "\033[34m  pip install smtplib  \033[0m"
  pip install -y smtplib
  echo "\033[34m  pip install twilio  \033[0m"
  pip install -y twilio
#  brew tap twilio/brew && brew install twilio

  sleep 5

  echo "\033[34m  Setting up CronTab  \033[0m"
  . _crontab.sh

  sleep 2

  echo "\033[34m  when finished I'll change the -1 to 1  \033[0m"
  . setup_complete.sh
  
  sleep 2
fi

echo -e "\n\n"

duration=$SECONDS
echo "\033[34m  Script_setup.sh Ran in $(($duration / 60)) minutes and $(($duration % 60)) seconds.  \033[0m"
