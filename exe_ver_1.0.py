import setup
import time
import sys, traceback
from traceback import extract_tb
import RPi.GPIO as GPIO

from HC_SR04_class import HC_SR04
import email__ as email


def GPIO_setup():
    GPIO.setmode(GPIO.BCM)

    hc_sr04 = HC_SR04()

    print('\n\n'
          f'\033[31m\033[43m============================================\033[0m\n'
          f'\033[31m\033[43m           Running exe_ver_1.0.py           \033[0m\n'
          f'\033[31m\033[43m         Any Thoughts on the Color?         \033[0m\n'
          f'\033[31m\033[43m============================================\033[0m\n'
          f'\n')

    print("Distance Measurement in Progress\n")
    GPIO.setup(hc_sr04.TRIG, GPIO.OUT)
    GPIO.setup(hc_sr04.ECHO, GPIO.IN)

    return hc_sr04


def find_distance_and_percent(hc_sr04, pulse_end, pulse_start):
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)
    distance_away = hc_sr04.size_of_container - distance

    percent_left = ((distance_away / hc_sr04.size_of_container) * 100)
    percent_left = round(percent_left, 2)

    return distance, percent_left


def main():
    message = None

    try:
        hc_sr04 = GPIO_setup()
        while True:

            GPIO.output(hc_sr04.TRIG, False)
            print("Waiting For Sensor To Settle\n")
            time.sleep(2)

            GPIO.output(hc_sr04.TRIG, True)
            time.sleep(0.0001)
            GPIO.output(hc_sr04.TRIG, False)

            pulse_start, pulse_end = 0, 0
            while GPIO.input(hc_sr04.ECHO) == 0:
                pulse_start = time.time()

            while GPIO.input(hc_sr04.ECHO) == 1:
                pulse_end = time.time()

            distance, percent_left = find_distance_and_percent(hc_sr04, pulse_end, pulse_start)

            if hc_sr04.send_notification(percent_left):
                email.send_report(percent_left)

            print(f"Percent Remaining: {percent_left}%")
            print(f"Distance: {distance} cm")

    except KeyboardInterrupt:  # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program
        message = 'KeyboardInterrupt'  # message = e.traceBack() etc.

    except FileNotFoundError:
        message = 'FileNotFoundError'

    except NameError:
        message = 'NameError'

#    I want to pass the `e` in there like in Java so the email contains the Info
    finally:
        print("\nCleaning up!")
        GPIO.cleanup()
        if message is None:
            message = 'UnKnown Error'

        trace_back = traceback.format_exception(*sys.exc_info())  # .print_exc(file=sys.stdout)
        formated_exe = ""
        for i in trace_back:
            formated_exe = f"{formated_exe}{i}"
        email.send_exception_error(message, formated_exe)

        sys.exit()


if __name__ == '__main__':
    setup.setup()
    main()
