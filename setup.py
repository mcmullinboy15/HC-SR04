import os
import csv

''' Imports '''

setup_file = 'user_data.csv'


def setup_complete(change_value=False):
    this = 1

    if change_value:
        read = open(setup_file, 'r+')
        text = read.read()
        text = text.replace(str(-1), str(1))

        file = open(setup_file, 'w')
        file.write(text)
        file.close()

        read.close()
    else:
        file = open(setup_file, 'r')
        reader = csv.DictReader(file)
        for line in reader:
            this = int(line['setup_complete'])
        file.close()
    return this < 0


def setup():
    if setup_complete():
        os.system("source script_setup.sh ")
        setup_complete(change_value=True)

if __name__ == '__main__':
    setup()
