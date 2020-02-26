

#   https://raspberrypi.stackexchange.com/questions/88150/how-to-install-python-3-7-with-ssl
#   pip /  pip3.7 is super ugly

  sleep 10
# echo "q"
  sudo apt-get -y update
  sudo apt-get -y upgrade
  sudo apt-get -y dist-upgrade
  sudo apt-get -y install build-essential checkinstall python-dev python-setuptools python-pip python-smbus
  sudo apt-get -y install libreadline-gplv2-dev libncursesw5-dev libgdbm-dev libc6-dev libbz2-dev
  sudo apt-get -y install zlib1g-dev libsqlite3-dev tk-dev
  sudo apt-get -y install libssl-dev openssl
  sudo apt-get -y install libffi-dev

  sleep 3

  cd /usr/src || exit
  sudo wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
  sudo sudo tar xzf Python-3.7.0.tgz

  sleep 2

  cd Python-3.7.0 || exit
  echo "bash configure" | sudo -s
  echo "make altinstall" | sudo -s

  sleep 2

  cd || exit
  echo "alias gs='git status'" >> .bash_aliases
  echo "alias python='python3.7'" >> .bash_aliases
  echo "alias python3='python3.7'" >> .bash_aliases
  echo "alias pip='pip3.7'" >> .bash_aliases
  echo "alias pip3='pip3.7'" >> .bash_aliases
  . ~/.bashrc

  sleep 2

  pip install --user pi --upgrade pip

  sleep 10

#  sudo rm -rf Python-3.7.6
#  rm -rf Python-3.7.6.tar.xz

#  sudo apt-get autoremove
#  sudo apt-get clean