import math
import datetime as date
import csv

USER_DATA_fn = 'user_data.csv'


class HC_SR04:

    def __init__(self, size_of_container=121.9, TRIG=23, ECHO=24, today='2020-01-24'):
        file = open(USER_DATA_fn)
        self.user_data = csv.DictReader(file)
        for row in self.user_data:
            self.TIME_OF_DAY = float(row['time_of_day'])
            print('time_of_day =', self.TIME_OF_DAY)

            self.size_of_container = float(row['size_of_container'])  # 121.9cm is 4ft
            self.send_daily = row['send_daily']

            # These are to be implemented
            self.single_noti_1 = float(row['single_noti_1'])
            self.single_noti_2 = float(row['single_noti_2'])
            self.single_noti_3 = float(row['single_noti_3'])
            self.daily_noti = float(row['daily_noti'])
        file.close()

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

        # These are to be implemented
        # self.send_daily
        # self.single_noti_1
        # self.single_noti_2
        # self.single_noti_3
        # self.daily_noti

        today_temp = date.datetime.today() - date.timedelta(hours=self.TIME_OF_DAY)
        today_temp = today_temp.date()
        if today_temp > self.today:

            percents_to_send_at = [15]  # [50, 30, 15, 10, 5, 3, 2]
            if True: # percent_left in percents_to_send_at:
                self.today = today_temp
                return True
            else:
                return False
        else:
            return False
