import setup
import time
import RPi.GPIO as GPIO

from HC_SR04_class import HC_SR04
import email_testing as email


def GPIO_setup():
    # import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)

    hc_sr04 = HC_SR04()
    TRIG = hc_sr04.TRIG
    ECHO = hc_sr04.ECHO
    size_of_container = hc_sr04.size_of_container

    '''Main'''
    print("Distance Measurement in Progress")
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

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
    try:
        hc_sr04 = GPIO_setup()
        while True:

            GPIO.output(hc_sr04.TRIG, False)
            print("Waiting For Sensor To Settle")
            time.sleep(1)  # 2)

            GPIO.output(hc_sr04.TRIG, True)
            time.sleep(0.0001)
            GPIO.output(hc_sr04.TRIG, False)

            pulse_start = 0
            pulse_end = 0
            while GPIO.input(hc_sr04.ECHO) == 0:
                pulse_start = time.time()

            while GPIO.input(hc_sr04.ECHO) == 1:
                pulse_end = time.time()

            distance, percent_left = find_distance_and_percent(hc_sr04, pulse_end, pulse_start)

            if hc_sr04.send_notification(percent_left):
                email.send_email(percent_left)

            print(f"Percent Remaining: {percent_left}%")
            print("Distance: " + str(distance) + " cm")

    except KeyboardInterrupt:  # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program
        print("\nCleaning up!")
        GPIO.cleanup()


if __name__ == '__main__':
    print('1')
    setup.import_necessary_libraries()
    main()
