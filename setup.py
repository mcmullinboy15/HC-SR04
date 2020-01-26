import os

''' Imports '''


def import_necessary_libraries():
    'This is the impost for the Sensor'
    'import RPi.GPIO as GPIO'
    os.system('pip install RPi.GPIO')

    'This might not be needed but connects to gmail server'
    'import smtplib'
    os.system('pip install smtplib')

    "I Hope this works, I don't use it yet but might in the future"
    'import pandas as pd'
    os.system('sudo apt-get install python-pandas')

if __name__ == '__main__':
    import_necessary_libraries()