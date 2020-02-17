
USERNAME='oldfarm'
PASSWORD='OldFarmpa$$'

WIFI_DIR='/etc/wpa_supplicant/wpa_supplicant.conf'

echo "setting up wifi"
sudo rfkill unblock 0
sudo ifconfig wlan0 up

printf -v var "
country=US\\\\n\\\\n
network={\\\\n
\\\t\tssid=%s\\\\n
\\\t\tscan_ssid=1\\\\n
\\\t\tpsk=%s\\\\n
}" $USERNAME $PASSWORD

echo $var >> $WIFI_DIR

wpa_cli -i wlan0 reconfigure

path="$HOME/Documents/EZ_Salt/HC-SR04"
if [ -d "$path" ]
then
  echo "Directory $path exists."
  cd "$HOME"/Documents/EZ_Salt/HC-SR04/ || return

else
  echo "creating path to repo"
  mkdir -p ~/Documents/EZ_Salt
  cd "$HOME"/Documents/EZ_Salt/ || return

  echo "cloning the git repo from ezsaltdevenv/HC-SR04.git"
  git clone https://ezsaltdevenv:ezsalt98@github.com/ezsaltdevenv/HC-SR04.git

  echo "entering git repo"
  cd "$HOME"/Documents/EZ_Salt/HC-SR04/ || return
fi