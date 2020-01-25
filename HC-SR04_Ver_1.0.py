import math
import RPi.GPIO as GPIO
import time
import datetime as date

from HC_SR04_class import HC_SR04

GPIO.setmode(GPIO.BCM)

import email_testing as email

hc_sr04 = HC_SR04()
TRIG = hc_sr04.TRIG
ECHO = hc_sr04.ECHO
size_of_container = hc_sr04.size_of_container


'''Main'''
print("Distance Measurement in Progress")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
try:
    while True:

        GPIO.output(TRIG, False)
        print("Waiting For Sensor To Settle")
        time.sleep(1)  # 2)

        GPIO.output(TRIG, True)
        time.sleep(0.0001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)
        distance_away = size_of_container - distance

        percent_left = ((distance_away / size_of_container) * 100)
        percent_left = round(percent_left, 2)

        if hc_sr04.send_notification(percent_left):
            email.send_email(percent_left)

        print(f"Percent Remaining: {percent_left}%")
        print("Distance: " + str(distance) + " cm")

except KeyboardInterrupt:  # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program
    print("Cleaning up!")
    gpio.cleanup()
