import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import email
import os.path
import csv

# import pandas as pd

"""
Article about SMS
https://www.nexmo.com/blog/2019/03/21/sending-sms-from-python-with-google-cloud-functions-dr
"""






class Email():
    """ Sending Multiple Messages """
    """ Received from: [ https://nitratine.net/blog/post/how-to-send-an-email-with-python/ ] """

    def __init__(self):
        self.email = 'ezsalt.dev.env@gmail.com'
        self.password = 'ezsalt98'
        self.attach_file = False
        self.USER_DATA_fn = 'user_data.csv'
        self.server = self.connect()

        self.name_list = list()
        self.part = None

        # Eventually I want to store all errors but not neccessary.
        # I think I just need to remember that I am using the same file everytime there is an email sent out
        self.csv_location = 'attach.csv'
        self.txt_location = 'attach.txt'

        for row in csv.DictReader(open('message_content.csv')):
            self.message_dict = row

        # This is the structure of the messages
        self.subject = '[ SUBJECT HERE ]'
        self.header = '[ HEADER ]'
        self.message = '[ MESSAGE ]'
        self.data = '[ DATA ]'

        self.carriers = {
                'att'    : '@mms.att.net',
                'tmoblie': '@tmomail.net',
                'verizon': '@vtext.com',
                'sprint' : '@page.nextel.com'
        }
        self.send_emails_to = ['ezsalt.dev.env@gmail.com']  # , 'mcmullinboy15@gmail.com']

    def send_exception_error(self, error, traceback):
        self.subject = error
        self.header = self.message_dict['header']
        self.message = self.message_dict['exception_message']
        self.data = traceback
        self.send_email(False)

    def send_report(self, percent):  # List of email addresses

        self.subject = self.message_dict['report_subject']
        self.header = self.message_dict['header']
        self.message = f'This is an message to let you know that you water ' \
                f'softener salt is almost out of salt!\n\n' \
                f'You currently have {round(percent)}% salt remaining ' \
                f'in your tank.\n\n' \
                f'https://square.site/book/RF2BTQNX9JXWK/ezsalt' \
                f'\n\nClick here to schedule a salt delivery.\n ' \
                f'\nThank You and have a Great day!!'

        self.data = f'percent, {percent}\n' \
            f'height, {4}\n' \
            f'max_capacity, {3}\n' \
            f'bags_to_fill, {1.33}\n' \
            f''
        self.send_email(True)

    def send_email(self, is_report=False):

        file = open(self.USER_DATA_fn)
        csv_data = csv.DictReader(file)

        # also append 'EZ_SALT'
        for row in csv_data:
            name = str(row['name'])
            names = name.split(',')
            for name in names:
                if name != '':
                    self.name_list.append(name)

            email_temp = str(row['email'])
            emails = email_temp.split(',')
            for _email_ in emails:
                if _email_ != '':
                    self.send_emails_to.append(_email_)
                    # send_emails_to = email_list
        file.close()

        file_location = self.txt_location
        if is_report:
            file_location = self.csv_location

        if self.attach_file:
            self.writetofile(file_location)
            self.create_attachment(file_location)

        self.send()

    def writetofile(self, file_location):
        attaching = open(file_location, 'w')
        # attaching.write(str(self.header))
        attaching.write(str(self.data))
        attaching.close()

    # This file wants to be opened in html reader when it is a .txt ... Fix that Andrew
    def create_attachment(self, file_location):
        # Create the attachment file (only do it once)
        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        self.part = MIMEBase('application', 'octet-stream')
        self.part.set_payload(attachment.read())
        encoders.encode_base64(self.part)
        self.part.add_header('Content-Disposition', "attachment; filename= %s" % filename)


    def connect(self):
        # Connect and login to the email server
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.email, self.password)
        return self.server


    def send(self):
        """ Loop over each email to send to """

        print(self.name_list)
        print(self.send_emails_to)
        counter = 0
        for send_to_email in self.send_emails_to:  # Lets to this :: for sent_to_email, name in list_of_people:

            print(send_to_email)
            print(self.subject)
            print(self.header + '\n' + self.message)

            # Setup MIMEMultipart for each email address (if we don't do this, the emails will concat on each email sent)
            msg = MIMEMultipart()

            msg['From'] = str(self.email)
            msg['To'] = str(send_to_email)
            msg['Subject'] = str(self.subject)

            # Attach the message to the MIMEMultipart object
            msg.attach(MIMEText(self.header + self.name_list[counter] + '\n' + self.message, 'plain'))

            # Attach the attachment file
            # TODO attach if it is an email not a text
            if self.part is not None:
                msg.attach(self.part)

            # Send the email to this specific email address
            self.server.sendmail(str(self.email), str(send_to_email), msg.as_string())
            counter += 1


    def done(self):
        """ Quit the email server when everything is done """
        self.server.quit()
