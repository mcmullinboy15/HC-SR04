

#   https://raspberrypi.stackexchange.com/questions/88150/how-to-install-python-3-7-with-ssl
#   pip /  pip3.7 is super ugly

  sleep 10
# echo "q"
  echo "apt-get update [python]"
  sudo apt-get -y update
  echo "apt-get upgrade [python]"
  sudo apt-get -y upgrade
  echo "apt-get dist-upgrade"
  sudo apt-get -y dist-upgrade
  echo "apt-get -y install build-essential checkinstall python-dev python-setuptools python-pip python-smbus"
  sudo apt-get -y install build-essential checkinstall python-dev python-setuptools python-pip python-smbus
  echo "apt-get -y install libreadline-gplv2-dev libncursesw5-dev libgdbm-dev libc6-dev libbz2-dev"
  sudo apt-get -y install libreadline-gplv2-dev libncursesw5-dev libgdbm-dev libc6-dev libbz2-dev
  echo "apt-get -y install zlib1g-dev libsqlite3-dev tk-dev"
  sudo apt-get -y install zlib1g-dev libsqlite3-dev tk-dev
  echo "apt-get -y install libssl-dev openssl"
  sudo apt-get -y install libssl-dev openssl
  echo "apt-get -y install libffi-dev"
  sudo apt-get -y install libffi-dev

  sleep 3

  cd /usr/src || exit
  sudo "sudo wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz"
  sudo wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
  echo "sudo sudo tar xzf Python-3.7.0.tgz"
  sudo sudo tar xzf Python-3.7.0.tgz

  sleep 2

  cd Python-3.7.0 || exit
  echo "sudo -s :: bash configure"
  echo "bash configure" | sudo -s
  echo "make altinstall"
  echo "sudo -s :: make altinstall" | sudo -s

  sleep 2

  cd || exit
  echo "setting aliases"
  echo "alias gs='git status'" >> .bash_aliases
  echo "alias python='python3.7'" >> .bash_aliases
  echo "alias python3='python3.7'" >> .bash_aliases
  echo "alias pip='pip3.7'" >> .bash_aliases
  echo "alias pip3='pip3.7'" >> .bash_aliases
  . ~/.bashrc

  sleep 2

  echo "Updating  pip3.7 to the funky pip"
  echo "pip install --user pi --upgrade pip"
  pip install -y --user pi --upgrade pip

  sleep 10

#  sudo rm -rf Python-3.7.6
#  rm -rf Python-3.7.6.tar.xz

#  sudo apt-get autoremove
#  sudo apt-get clean