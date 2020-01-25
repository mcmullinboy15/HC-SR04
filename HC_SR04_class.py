import math
import datetime as date


class HC_SR04:
    def __init__(self, size_of_container=121.9, TRIG=23, ECHO=24, today='2020-01-24'):
        self.size_of_container = size_of_container  # cm is 4ft

        self.TRIG = TRIG
        self.ECHO = ECHO

        '2020-01-24 14:00:00.000000'
        self.today = today  # date.datetime.today() - date.timedelta(hours=24)
        print(self.today)

    def roundup(self, x):
        return int(math.ceil(x / 10.0)) * 10

    #    send an [ email, text, notification, etc. ]
    #    Look up how to send the email.  Could use GSuite.
    def send_notification(self, percent_left):
        percent_left = self.roundup(percent_left)
        print(percent_left)

        if date.datetime.today() != self.today:  # >
            self.today = date.datetime.today()
        else:
            return False

        percents_to_send_at = [50, 30, 15, 10, 5, 3, 2]
        if percent_left in percents_to_send_at:
            return True
        else:
            return False
