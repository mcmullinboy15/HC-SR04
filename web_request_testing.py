import requests
import csv

id_file = "25_id.txt"

USER_DATA_fn = 'user_data.csv'


def attack_website(distance):
    Token = 'F84JB70M9G71A54HV64HG73JZ'

    try:
        f = open(id_file, 'r')

        # print(f.read())

        code = f.read()
        print(code)

        # if there is a 25 digit thing inside the file
        url = f"http://ezsalt.services/API.php?Token={Token}&Code={code}&Distance={distance}"

        print(url)
        r = requests.get(url=url)
        print(r.text)

    except IOError:
        print("File does not exist")

        f = open(USER_DATA_fn)
        user_data = csv.DictReader(f)
        email = None
        for row in user_data:
            email = row['email']

        url = f"http://ezsalt.services/API.php?Token={Token}&Email={email}"

        print(url)
        r = requests.get(url=url)
        print(r.text)
        code_ = r.text

        f = open(id_file, 'w')
        f.write(str(code_))

    finally:
        f.close()

    return r


attack_website(120.3)
