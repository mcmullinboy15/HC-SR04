import setup
import time
import RPi.GPIO as GPIO

from HC_SR04_class import HC_SR04
import email_testing as email


def GPIO_setup():
    GPIO.setmode(GPIO.BCM)

    hc_sr04 = HC_SR04()

    print(f'\n\033[47m\n'
          f'\033[31m============================================\033[0m\n\n'
          f'\033[31m           Running exe_ver_1.0.py           \033[0m\n'
          f'\033[31m         Any Thoughts on the Color?         \033[0m\n\n'
          f'\033[31m============================================\033[0m\033[0m\n\n')

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
    global message

    try:
        hc_sr04 = GPIO_setup()
        while True:

            GPIO.output(hc_sr04.TRIG, False)
            print("Waiting For Sensor To Settle")
            time.sleep(1)  # 2)

            GPIO.output(hc_sr04.TRIG, True)
            time.sleep(0.0001)
            GPIO.output(hc_sr04.TRIG, False)

            pulse_start, pulse_end = 0, 0
            print('pulse', pulse_start, pulse_end)
            while GPIO.input(hc_sr04.ECHO) == 0:
                pulse_start = time.time()

            while GPIO.input(hc_sr04.ECHO) == 1:
                pulse_end = time.time()

            distance, percent_left = find_distance_and_percent(hc_sr04, pulse_end, pulse_start)

            if hc_sr04.send_notification(percent_left):
                email.send_report(percent_left)

            print(f"Percent Remaining: {percent_left}%")
            print("Distance: " + str(distance) + " cm")

    except KeyboardInterrupt:  # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program
        print("\nCleaning up!")
        GPIO.cleanup()
        message = 'KeyboardInterrupt'  # message = e.traceBack() etc.

    except FileNotFoundError:
        message = 'FileNotFoundError'

    finally:
        print("\nCleaning up!")
        GPIO.cleanup()

        email.send_exception_error(message)
        # I want to pass the `e` in there like in Java so the email contains the Info


if __name__ == '__main__':
    setup.setup()
    main()
