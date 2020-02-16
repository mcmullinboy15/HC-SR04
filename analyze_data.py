from email__ import Email


# TODO  This is not  used yet
def send_data(hc_sr04, distance, percent_left):

    email = Email()
    #    sending email
    if hc_sr04.send_notification(percent_left):
        email.send_report(percent_left)

    #    send the data to the database
