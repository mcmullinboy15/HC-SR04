import email__ as email


# TODO  This is not  used yet
def send_data(hc_sr04, distance, percent_left):
    #    send the data to the database

    #    sending email
    if hc_sr04.send_notification(percent_left):
        email.send_report(percent_left)
