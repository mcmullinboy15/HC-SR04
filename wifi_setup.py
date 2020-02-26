import csv
import os


USER_DATA_fn = 'user_data.csv'
WIFI_DIR = '/etc/wpa_supplicant/wpa_supplicant.conf'

print(f"adding wifi credentials on {os.uname()[1]}")
if os.uname()[1].__contains__('pi'):

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
    os.system('echo "sudo rfkill unblock 0"')
    os.system("sudo rfkill unblock 0")
    os.system('echo "sudo ifconfig wlan0 up"')
    os.system("sudo ifconfig wlan0 up")

    os.system(f'echo "adding  wifi credentials to {WIFI_DIR}"')
    os.system(f"echo {PASSWORD} | wpa_passphrase {USERNAME} | sudo tee -a {WIFI_DIR} > /dev/null")

    os.system(f"echo $var >> {WIFI_DIR}") # I might want to delete that

    os.system('echo "wpa_cli -i wlan0 reconfigure"')
    os.system("wpa_cli -i wlan0 reconfigure")


else:
    print("\n\n THE USERNAME [ os.uname()[1] ] doesn't contain pi")
    os.system("sleep 10")