import RPi.GPIO as GPIO
import time

pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

def detection(pin):
    if GPIO.input(pin):
        print("Motion Detected")
    else:
        print("Motion Detected")

GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(pin, detection)

while True:
    time.sleep(1)
