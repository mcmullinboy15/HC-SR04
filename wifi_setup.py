import csv
import os


USER_DATA_fn = 'user_data.csv'
WIFI_DIR = '/etc/wpa_supplicant/wpa_supplicant.conf'

print(f"adding wifi credentials on {os.uname()[1]}")
if os.uname()[1] == 'pi':

    file = open(USER_DATA_fn)
    data = csv.DictReader(file)
    print(data.fieldnames)

    USERNAME = None
    PASSWORD = None
    for row in data:
        USERNAME = row['WIFI_username']
        PASSWORD = row['WIFI_password']
    file.close()

    os.system("echo 'setting up user's wifi'")
    os.system("sudo rfkill unblock 0")
    os.system("sudo ifconfig wlan0 up")

    os.system(f"echo {PASSWORD} | wpa_passphrase {USERNAME} | sudo tee -a {WIFI_DIR} > /dev/null")

    os.system(f"echo $var >> {WIFI_DIR}") #sudo
    os.system("wpa_cli -i wlan0 reconfigure")


else:
    print("\n\n THE USERNAME [ os.uname()[1] ] isn't  pi")
    os.system("sleep 15")