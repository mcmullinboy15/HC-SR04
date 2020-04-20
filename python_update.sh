

#   https://raspberrypi.stackexchange.com/questions/88150/how-to-install-python-3-7-with-ssl
#   pip /  pip3.7 is super ugly

#   https://gist.github.com/SeppPenner/6a5a30ebc8f79936fa136c524417761dr
#   Another option. We'll see

  sleep 10
# echo "q"

  echo -e "\033[34m  apt-get dist-upgrade  \033[0m"
  sudo apt-get -y dist-upgrade
  echo -e "\033[34m  apt-get -y install build-essential checkinstall python-dev python-setuptools python-pip python-smbus  \033[0m"
  sudo apt-get -y install build-essential checkinstall python-dev python-setuptools python-pip python-smbus
  echo -e "\033[34m  apt-get -y install libreadline-gplv2-dev libncursesw5-dev libgdbm-dev libc6-dev libbz2-dev  \033[0m"
  sudo apt-get -y install libreadline-gplv2-dev libncursesw5-dev libgdbm-dev libc6-dev libbz2-dev
  echo -e "\033[34m  apt-get -y install zlib1g-dev libsqlite3-dev tk-dev  \033[0m"
  sudo apt-get -y install zlib1g-dev libsqlite3-dev tk-dev
  echo -e "\033[34m  apt-get -y install libssl-dev openssl  \033[0m"
  sudo apt-get -y install libssl-dev openssl
  echo -e "\033[34m  apt-get -y install libffi-dev  \033[0m"
  sudo apt-get -y install libffi-dev

  sleep 3

  cd /usr/src || exit
  echo -e "\033[34m  sudo wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz  \033[0m"
  sudo wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
  echo -e "\033[34m  sudo sudo tar xzf Python-3.7.0.tgz  \033[0m"
  sudo sudo tar xzf Python-3.7.0.tgz

  sleep 2

  cd Python-3.7.0 || exit
  echo -e "\033[34m  sudo -s :: bash configure  \033[0m"
  echo "bash configure" | sudo -s
  echo -e "\033[34m  sudo -s :: make altinstall  \033[0m"
  echo "make altinstall" | sudo -s

  sleep 2

  cd || exit
  echo -e "\033[34m  setting aliases  \033[0m"
  echo "alias gs='git status'" >> .bash_aliases
  echo "alias python='python3.7'" >> .bash_aliases
  echo "alias python3='python3.7'" >> .bash_aliases
  echo "alias pip='pip3.7'" >> .bash_aliases
  echo "alias pip3='pip3.7'" >> .bash_aliases
  . ~/.bashrc

  sleep 2

  echo -e "\033[34m  Updating  pip3.7 to the funky pip  \033[0m"
  echo -e "\033[34m  pip install --user pi --upgrade pip  \033[0m"
  pip install -y --user pi --upgrade pip

  sleep 10

#  sudo rm -rf Python-3.7.6
#  rm -rf Python-3.7.6.tar.xz

#  sudo apt-get autoremove
#  sudo apt-get clean