import RPi.GPIO as GPIO
import time
from gpiozero import Buzzer

#if arm = TRUE tab everything over
buzzer = Buzzer(24)
pin = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

def detection(pin):
    if GPIO.input(pin):
        print("Sound Detected")
        buzzer.on()
        time.sleep(1)
    else:
        print("Sound Detected")

GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(pin, detection)

while True:
    time.sleep(1)

