from twilio.rest import Client
import csv


# def get_carrier():

f = open('user_data.csv')
file = csv.DictReader(f)
number = None
for line in file:
    number = line['phone_number']
numbers = number.split(",")


client = Client(username='AC2852e287bb7e3eab92b59aefd428f5ce', password='909dbd30121e0556048ad0c0b40972ec')

carriers = []
for number_ in numbers:
    phone_number = client.lookups \
        .phone_numbers(number_) \
        .fetch(type='carrier')

    carriers.append(phone_number.carrier['name'])  # Just the carrier name.
# return carriers

print(carriers)

# get_carrier()

