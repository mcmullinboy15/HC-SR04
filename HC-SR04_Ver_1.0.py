import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

size_of_container = 121.9 #cm is 4ft 

TRIG = 23
ECHO = 24


def send_notification(percent_left):
    percent_left = round(percent_left, 1)
    print(percent_left)
    percents_to_send_at = [50, 30, 15, 10, 5, 3, 2]
    if percent_left in percents_to_send_at:
        #




print("Distance Measurement in Progress")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
try:
    while True:
        
        GPIO.output(TRIG, False)
        print("Waiting For Sensor To Settle")
        time.sleep(1) # 2)
        
        GPIO.output(TRIG, True)
        time.sleep(0.0001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
            
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
            
        pulse_duration = pulse_end - pulse_start
        
        distance = pulse_duration * 17150        
        distance = round(distance, 2)
        distance_away = size_of_container-distance

        percent_left = ((distance_away/size_of_container)*100)
        percent_left = round(percent_left, 2)

        if send_notification(percent_left):
            send_email(percent_left)

        print(f"Percent Remaining: {percent_left}%")
        print("Distance: "+ str(distance) + " cm")
        
except KeyboardInterrupt:  # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program
    print("Cleaning up!")
    gpio.cleanup()
