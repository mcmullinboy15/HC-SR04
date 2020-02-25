

#   https://raspberrypi.stackexchange.com/questions/88150/how-to-install-python-3-7-with-ssl
#   pip /  pip3.7 is super ugly

  sleep 10

  sudo apt-get update
  sudo apt-get upgrade
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
  sudo -s
  bash configure
  make altinstall
  exit

  sleep 5

  pip install --user pi --upgrade pip
  cd || exit

  sleep 10

#  sudo rm -rf Python-3.7.6
#  rm -rf Python-3.7.6.tar.xz

#  sudo apt-get autoremove
#  sudo apt-get clean