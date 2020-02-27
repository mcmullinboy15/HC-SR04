#!/bin/sh

#setting up the USB
#   sudo mkdir /media/usb
#   sudo chown -R pi:pi /media/usb
#   sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi
#   cd /media/usb
#   source Sam.sh

USERNAME='oldfarm'
PASSWORD='OldFarmpa$$'

WIFI_DIR='/etc/wpa_supplicant/wpa_supplicant.conf'

echo "setting up wifi"
sudo rfkill unblock 0
sudo ifconfig wlan0 up

echo $PASSWORD | wpa_passphrase $USERNAME | sudo tee -a $WIFI_DIR > /dev/null

#echo $var >> $WIFI_DIR #sudo

wpa_cli -i wlan0 reconfigure

path="$HOME/Documents/EZ_Salt/HC-SR04"
if [ -d "$path" ]
then
  echo "Directory $path exists."
  cd "$HOME"/Documents/EZ_Salt/HC-SR04/ || return

else
  echo "creating path to repo"
  mkdir -p "$HOME"/Documents/EZ_Salt
  cd "$HOME"/Documents/EZ_Salt/ || return

  sleep 30

  echo "cloning the git repo from ezsaltdevenv/HC-SR04.git"
  git clone https://ezsaltdevenv:ezsalt98@github.com/ezsaltdevenv/HC-SR04.git

  echo "entering git repo"
  cd "$HOME"/Documents/EZ_Salt/HC-SR04/ || return
fi

sleep 10


