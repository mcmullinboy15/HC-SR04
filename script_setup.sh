#!/bin/sh

if [ $(source setup_complete.sh) = 'true' ]
then
  echo "Setup has Already  been run so  we will not do that now"
else
  python3 wifi_setup.py

  echo "updating raspberry pi"
  #sudo apt update
  #sudo apt full-upgrade

  path="../../../Documents/EZ_Salt/HC-SR04"
  if [ -d "$path" ]
  then
    echo "Directory $path exists."
    cd ~/Documents/EZ_Salt/HC-SR04/ || return

  else
    echo "creating path to repo"
    mkdir -p ~/Documents/EZ_Salt
    cd ~/Documents/EZ_Salt/ || return


    echo "assigning username and password"
    git config --global user.name "ezsaltdevenv"
    git config --global user.password "ezsalt98"

    echo "cloning the git repo from ezsaltdevenv/HC-SR04.git"
    git clone https://github.com/ezsaltdevenv/HC-SR04.git

    echo "entering git repo"
    cd ~Documents/EZ_Salt/HC-SR04/ || return
  fi

  echo
  echo "changing terminal design temporarily"
  #chsh -s /bin/bash
  #'This has the pi@raspberry tag'
  #os.system("export PS1='\[\033[32m\]\[\033[m\]@\[\033[32m\] \[\033[33;1m\]\w\[\033[m\] (\$(git branch 2>/dev/null | grep '^*' | colrm 1 2)) $ '")
  #'This has the time as the tag'
  export PS1='\[\033[0;32m\]\[\033[0m\033[0;32m\][\@]\[\033[0;33m\]\w\[\033[0;36m\]$(__git_ps1)\n\[\033[0;32m\]\[\033[0m\033[0;32m\]\$\[\033[0m\033[0;32m\]\[\033[0m\] '

  echo
  echo "installing the nesseccary libraries"
  pip install RPi.GPIO
  pip install smtplib
  echo "not going to instal 'apt-get install python-pandas'"
  #sudo apt-get install python-pandas

  echo "when finished I'll change the -1 to 1"
  #python3 setup.py
  source setup_complete.sh
fi
echo
