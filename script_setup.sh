#!/bin/sh


if [ $(source setup_complete.sh) = 'true' ]
then
  echo "Setup has Already been run so we will not do that now"
else

  echo "updating raspberry pi"
  sudo apt update
  echo 'q' | echo 'Y' | sudo apt full-upgrade #1+ hour
  sudo apt-get update
  sudo apt-get upgrade

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
  #

# see if the updats above get python3 working
  echo "upgrading python"
  sudo apt-get update
  sudo apt-get install
  echo "Y" | sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.4-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev

  wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tgz
  tar -zxvf Python-3.7.6.tgz
  cd Python-3.7.6
  ./configure
  make
  sudo make altinstall

  sudo rm -r Python-3.7.6
  rm Python-3.7.6.tar.xz
  sudo apt-get --purge remove build-essential tk-dev
  sudo apt-get --purge remove libncurses5-dev libncursesw5-dev libreadline6-dev
  sudo apt-get --purge remove libdb5.4-dev libgdbm-dev libsqlite3-dev libssl-dev
  sudo apt-get --purge remove libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
  sudo apt-get autoremove
  sudo apt-get clean

  cd
  echo "alias gs='git status'" >> .bash_aliases
  echo "alias python='python3.7'" >> .bash_aliases
  echo "alias python3='python3.7'" >> .bash_aliases
  echo "alias pip='pip3.7'" >> .bash_aliases
  echo "alias pip3='pip3.7'" >> .bash_aliases



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

  echo "setting up wifi"
  sudo rfkill unblock 0
  sudo ifconfig wlan0 up
  python3 wifi_setup.py
  wpa_cli -i wlan0 reconfigure

  echo
  echo "changing terminal design temporarily"
  #chsh -s /bin/bash
  #'This has the pi@raspberry tag'
  #os.system("export PS1='\[\033[32m\]\[\033[m\]@\[\033[32m\] \[\033[33;1m\]\w\[\033[m\] (\$(git branch 2>/dev/null | grep '^*' | colrm 1 2)) $ '")
  #'This has the time as the tag'
  export PS1='\[\033[0;32m\]\[\033[0m\033[0;32m\][\@]\[\033[0;33m\]\w\[\033[0;36m\]$(__git_ps1)\n\[\033[0;32m\]\[\033[0m\033[0;32m\]\$\[\033[0m\033[0;32m\]\[\033[0m\] '

  echo
  echo "installing the nesseccary libraries"
#  pip install RPi.GPIO
  echo "Y" | sudo apt-get install rpi.gpio
  pip install smtplib
  echo "not going to instal 'apt-get install python-pandas'"
  #sudo apt-get install python-pandas

  echo "when finished I'll change the -1 to 1"
  source setup_complete.sh
fi
echo
