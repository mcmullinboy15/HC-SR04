import os
import csv

''' Imports '''

setup_file = 'setup_variables.csv'


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


def import_necessary_libraries():
    run = setup_complete()
    # print('1', run)

    if run:
        'This is the impost for the Sensor'
        'import RPi.GPIO as GPIO'
        os.system('pip install RPi.GPIO')

        'This might not be needed but connects to gmail server'
        'import smtplib'
        os.system('pip install smtplib')

        "I Hope this works, I don't use it yet but might in the future"
        'import pandas as pd'
        os.system('sudo apt-get install python-pandas')

        print('2', setup_complete(change_value=True))


if __name__ == '__main__':
    import_necessary_libraries()
