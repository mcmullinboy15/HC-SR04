#!/bin/sh

# rpi.gpio
# right before not importing pandas

SECONDS=0

if [ "$(. is_setup_complete.sh)" = 'true' ]
then
  echo "Skipping Setup because its Already Done"
else
  echo "updating raspberry pi"

  echo "full-upgrade"
  echo 'q' | sudo apt -y full-upgrade #1+ hour
  echo  "apt-get update"
  sudo apt-get update
  echo "apt-get upgrade"
#  echo "" |      # It said the desktop might hvae changed press ok
  sudo apt-get -y upgrade --fix-missing

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

# see if the updats above get python3 working
  echo "upgrading python"
  sudo apt-get install
  . python_update.sh

  sleep 10

  path="$HOME/Documents/EZ_Salt/HC-SR04"
  if [ -d "$path" ]
  then
    echo "Directory $path exists."
    cd "$HOME"/Documents/EZ_Salt/HC-SR04/ || return

  else
    echo "creating path to repo"
    mkdir -p "$HOME"/Documents/EZ_Salt
    cd "$HOME"/Documents/EZ_Salt/ || return

    echo "cloning the git repo from ezsaltdevenv/HC-SR04.git"
    git clone https://ezsaltdevenv:ezsalt98@github.com/ezsaltdevenv/HC-SR04.git

    echo "entering git repo"
    cd "$HOME"/Documents/EZ_Salt/HC-SR04/ || return
  fi

  sleep 10

  echo "setting up user wifi"
  python3 wifi_setup.py

  sleep 20

  echo "changing terminal design temporarily"
  #chsh -s /bin/bash
  #'This has the pi@raspberry tag'    export PS1='\[\033[32m\]\[\033[m\]@\[\033[32m\] \[\033[33;1m\]\w\[\033[m\] (\$(git branch 2>/dev/null | grep '^*' | colrm 1 2)) $ '
  #'This has the time as the tag'
  export PS1='\[\033[0;32m\]\[\033[0m\033[0;32m\][\@]\[\033[0;33m\]\w\[\033[0;36m\]$(__git_ps1)\n\[\033[0;32m\]\[\033[0m\033[0;32m\]\$\[\033[0m\033[0;32m\]\[\033[0m\] '

  echo "installing the nesseccary libraries"
  echo "sudo apt-get -y install rpi.gpio"
  sudo apt-get -y install rpi.gpio
  pip install -y RPi.GPIO
  echo "pip install smtplib"
  pip install -y smtplib
  echo "pip install twilio"
  pip install -y twilio
#  brew tap twilio/brew && brew install twilio

  sleep 5

  echo "Setting up CronTab"
  . _crontab.sh

  sleep 2

  echo "when finished I'll change the -1 to 1"
  . setup_complete.sh
  
  sleep 2
fi

echo -e "\n\n"

duration=$SECONDS
echo "Script_setup.sh Ran in $(($duration / 60)) minutes and $(($duration % 60)) seconds."
