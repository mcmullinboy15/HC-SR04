import csv
import os

USER_DATA_fn = 'user_data.csv'
WIFI_DIR = '/etc/wpa_supplicant/wpa_supplicant.conf'

print(f"adding wifi credentials on {os.uname()[1]}")
if os.uname()[1] == 'pi':
    f = open(WIFI_DIR, "a+")

    file = open(USER_DATA_fn)
    data = csv.DictReader(file)
    print(data.fieldnames)

    USERNAME = None
    PASSWORD = None
    for row in data:
        USERNAME = row['WIFI_username']
        PASSWORD = row['WIFI_password']
    file.close()

    var = "network={\n\
        ssid="+USERNAME+"\n\
        scan_ssid=1\n\
        psk="+PASSWORD+"\n\
    }"
    print(var)
    # f.write(var)