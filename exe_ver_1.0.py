import os
import sys
import time
import traceback

from email__ import Email
from HC_SR04_class import HC_SR04

fake_start = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#             86%    72%    58%      50%    30%      15%       9%      7%      6%      4%
fake_end = [0.999, 0.998, 0.997, 0.99645, 0.995, 0.99395, 0.99355, 0.9934, 0.9933, 0.9932]

email = None

def GPIO_setup():
    GPIO.setmode(GPIO.BCM)

    hc_sr04 = HC_SR04()

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
    message = 'The message was not initialized'
    error = 'The Traceback was not initialized'

    color1 = '\033[31m'
    color2 = '\033[43m'
    end_color = '\033[0m\n'

    print('\n\n'
          f'{color1}{color2}============================================{end_color}'
          f'{color1}{color2}           Running exe_ver_1.0.py           {end_color}'
          f'{color1}{color2}         Any Thoughts on the Color?         {end_color}'
          f'{color1}{color2}============================================{end_color}'
          f'\n')

    print("Distance Measurement in Progress\n")

    try:
        if laptop_testing:
            hc_sr04 = HC_SR04()
        else:
            hc_sr04 = GPIO_setup()
        email = Email()

        i = 0
        if laptop_testing:
            while i < len(fake_start):
                hc_sr04, i = while_loop_content(hc_sr04, i)
        else:
            while True:
                hc_sr04, i = while_loop_content(hc_sr04, i)

    except KeyboardInterrupt as ki:  # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program
        error = ki
        message = 'KeyboardInterrupt'  # message = e.traceBack() etc.

    except FileNotFoundError as fnf:
        error = fnf
        message = 'FileNotFoundError'

    except NameError as ne:
        error = ne
        message = 'NameError'

    # else:
    #     email.send_exception_error("The else method has been called???\n"
    #                                "I don't know what happened, I wonder if the "
    #                                "raspberry pi died", "ELSE Problem")

    #    I want to pass the `e` in there like in Java so the email contains the Info
    finally:
        print("\nCleaning up!")
        if not laptop_testing:
            GPIO.cleanup()

        if message is 'The message was not initialized':
            message = 'UnKnown Error'
        if error is 'The error was not initialized':
            error = "Exception Unknown"

        # raise
        # trace_back = traceback.format_exception(*sys.exc_info())
        # trace_back = traceback.print_exc(file=sys.stdout)
        # trace_back = sys
        # formated_exe = trace_back
        # print(trace_back)
        # for i in trace_back:
        #     formated_exe = f"{formated_exe}{i}"
        email.send_exception_error(error=message, traceback=error)

        sys.exit()


def while_loop_content(hc_sr04, i):
    pulse_start, pulse_end = 0, 0
    if laptop_testing:
        pulse_end = fake_start[i]
        pulse_start = fake_end[i]

    else:
        GPIO.output(hc_sr04.TRIG, False)
        print("Waiting For Sensor To Settle\n")
        time.sleep(2)

        GPIO.output(hc_sr04.TRIG, True)
        time.sleep(0.0001)
        GPIO.output(hc_sr04.TRIG, False)

        while GPIO.input(hc_sr04.ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(hc_sr04.ECHO) == 1:
            pulse_end = time.time()

    distance, percent_left = find_distance_and_percent(hc_sr04, pulse_end, pulse_start)

    if do_anything(distance, percent_left):
        """ Deciding if I should send a notification  """
        print(percent_left)
        if hc_sr04.send_notification(percent_left):
            email.send_report(percent_left)
        print(f"Percent Remaining: {percent_left}%")
        print(f"Distance: {distance} cm")

    i += 1
    return hc_sr04, i


def do_anything(distance, percent_left):
    if percent_left < 0:
        return False
    if percent_left < 100:
        return False


if __name__ == '__main__':
    laptop_testing = False

    print(os.uname()[1])
    if not str(os.uname()[1]).__contains__('pi@raspberry'):
        laptop_testing = True
    if not laptop_testing:
        import RPi.GPIO as GPIO
    main()
