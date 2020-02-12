import math
import datetime as date


class HC_SR04:

    def __init__(self, size_of_container=121.9, TRIG=23, ECHO=24, today='2020-01-24'):
        self.size_of_container = size_of_container  # 121.9cm is 4ft

        self.TRIG = TRIG
        self.ECHO = ECHO

        'now&today: 2020-01-24 14:00:00.000000'
        'date: 2020-01-24'
        self.today = date.datetime.today() - date.timedelta(hours=32)
        self.today = self.today.date()

    def roundup(self, percent_left):
        return int(round(percent_left))

    #        send an [ email, text, notification banner, etc. ]
    #        Look into using GSuite.
    def send_notification(self, percent_left):
        percent_left = self.roundup(percent_left)
        print(percent_left)

        today_temp = date.datetime.today() - date.timedelta(hours=8)
        today_temp = today_temp.date()
        if today_temp > self.today:

            percents_to_send_at = [50, 30, 15, 10, 5, 3, 2]
            if percent_left in percents_to_send_at:
                self.today = today_temp
                return True
            else:
                return False
        else:
            return False
