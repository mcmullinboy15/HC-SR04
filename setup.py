import os
import csv

''' Imports '''

setup_file = 'setup_variables.csv'



def setup_complete(change_value=False):
    file = None
    var = False
    if change_value:
        read = open(setup_file, 'r')
        content = csv.DictReader(read)
        print('dic:',content)
        content_list = list(content)
        print('list:',content_list)
        
        file = open(setup_file, 'w')
        file.write(str(content_list))
        file.close()
        read.close()
    else:
        file = open(setup_file, 'r')
        reader = csv.DictReader(file)
        for line in reader:
            if line['setup_complete']:
                var = line['setup_complete']
        print(var)
    file.close()
    return var

def import_necessary_libraries():

    run = setup_complete()

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
        
        setup_complete(change_value=True)

if __name__ == '__main__':
    import_necessary_libraries()
