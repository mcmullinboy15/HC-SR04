#  echo "Y" | sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.4-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
  #sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

  sleep 10

  wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tgz
  tar -zxvf Python-3.7.6.tgz
  cd Python-3.7.6
  ./configure
  make
  sleep 5
  sudo make altinstall

  sleep 10

  sudo rm -rf Python-3.7.6
  rm -rf Python-3.7.6.tar.xz

#  sudo apt-get autoremove
#  sudo apt-get clean