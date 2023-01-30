import RPi.GPIO as GPIO
import time
#pi camera 
from picamera import PiCamera
camera = PiCamera()

#motion sensor pin
pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

def detection(pin):
    if GPIO.input(pin):
        print("Motion Detected")
        camera.capture('/home/pi/Desktop/PersonSpotted.jpg')
    else:
        pass

GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(pin, detection)

while True:
    time.sleep(1)
