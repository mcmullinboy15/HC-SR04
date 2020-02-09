''' Sending Multiple Messages '''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

# import pandas as pd

email = 'ezsalt.dev.env@gmail.com'
password = 'ezsalt98'

# Eventually I want to store all errors but not neccessary.
# I think I just need to remember that I am using the same file everytime there is an email sent out
csv_location = 'attach.csv'
txt_location = 'attach.txt'


def send_exception_error(error, traceback, attach_file=True, send_emails_to=None):
    subject = error
    header = 'There has been an Interuption and/or Error that has Occured' \
             '\nPlease Contact EZ_Salt Support at 801-897-3786\n\n'
    data = traceback  # backTrace, etc.
    send_email(subject, header, data, False, attach_file, send_emails_to)


def send_report(percent, attach_file=True, send_emails_to=None):  # List of email addresses

    subject = f'Test_04: Your Water Softener is {percent}% filled'
    header = f'Data about your Water Softener:\n'
    data = f'Percent, {percent}\n' \
           f'height, {4}\n' \
           f'max_capacity, {3}\n' \
           f'bags_to_fill, {1.33}\n'
    send_email(subject, header, data, True, attach_file, send_emails_to)


def send_email(subject, header, data, is_report=False, attach_file=True, send_emails_to=None):
    part = None

    if send_emails_to is None:
        send_emails_to = ['ezsalt.dev.env@gmail.com']  # , 'mcmullinboy15@gmail.com']
    else:
        send_emails_to.append('ezsalt.dev.env@gmail.com')

    file_location = txt_location
    if is_report:
        file_location = csv_location
    print(data)
    if attach_file:
        writetofile(file_location, header, data)
        part = create_attachment(file_location)
    server = connect()
    send(send_emails_to, subject=subject, first_line=header, message=data, server=server, part=part)


def writetofile(file_location, header, data):
    # TODO  I added this to make the file
    attaching = open(file_location, 'w')
    attaching.write(header)
    attaching.write(data)
    attaching.close()


# This file wants to be opened in html reader when it is a .txt ... Fix that Andrew
def create_attachment(file_location):
    # Create the attachment file (only do it once)
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    return part


def connect():
    # Connect and login to the email server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    return server


def send(send_to_emails, subject, first_line, message, server, part):
    # Loop over each email to send to
    for send_to_email in send_to_emails:
        # Setup MIMEMultipart for each email address (if we don't do this, the emails will concat on each email sent)
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        # Attach the message to the MIMEMultipart object
        msg.attach(MIMEText(first_line + '\n' + message, 'plain'))
        # Attach the attachment file
        msg.attach(part)

        # Send the email to this specific email address
        server.sendmail(email, send_to_email, msg.as_string())
    return server


def done(server):
    # Quit the email server when everything is done
    server.quit()


""" Received from: [ https://nitratine.net/blog/post/how-to-send-an-email-with-python/ ] """

'''
Most simple Setup:

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = 'myaddress@gmail.com'
password = 'password'
send_to_email = 'sentoaddreess@gmail.com'
subject = 'This is the subject' # The subject line
message = 'This is my message'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

 # Attach the message to the MIMEMultipart object
msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string() # You now need to convert the MIMEMultipart object to a string to send
server.sendmail(email, send_to_email, text)
server.quit()

'''

'''
Used for having an Attachment:

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

email = 'myaddress@gmail.com'
password = 'password'
send_to_email = 'sentoaddreess@gmail.com'
subject = 'This is the subject'
message = 'This is my message'
file_location = 'C:\\Users\\You\\Desktop\\attach.txt'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

# Setup the attachment
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# Attach the attachment to the MIMEMultipart object
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
'''
