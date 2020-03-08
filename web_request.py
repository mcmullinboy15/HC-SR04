import requests
import csv

id_file = "25_id.txt"
USER_DATA_fn = 'user_data.csv'


def attack_website(distance):
    Token = 'F84JB70M9G71A54HV64HG73JZ'

    try:
        f = open(id_file, 'r')
        code = f.read()
        f.close()

        url = f"http://ezsalt.services/API.php?Token={Token}&Code={code}&Distance={distance}"

        r = requests.get(url=url)
        print(r.text)

    except IOError:
        print("File does not exist")

        f = open(USER_DATA_fn)
        user_data = csv.DictReader(f)
        email = None
        for row in user_data:
            email = row['email']
        f.close()

        url = f"http://ezsalt.services/API.php?Token={Token}&Email={email}"

        r = requests.get(url=url)
        print(r.text)
        code_ = r.text

        f = open(id_file, 'w')
        f.write(str(code_))
        f.close()

    return r


attack_website(120.3)
