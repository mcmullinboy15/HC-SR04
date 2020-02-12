

echo "adding wifi credentials"
if [ $USER = 'pi' ]
then
    echo 'network={
        ssid="testing"
        scan_ssid=1
        psk="testingPassword"
    }' >> /etc/wpa_supplicant/wpa_supplicant.conf
fi