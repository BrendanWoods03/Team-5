import RPi.GPIO as GPIO
import time

#set sound as the GPIO pin the sound sensor is connected to
sound = 6

#set motion as the GPIO pin the motion sensor is connected to
motion = 24

#set the GPIO to broadcom mode
GPIO.setmode(GPIO.BCM)

#set the pins as inputs
GPIO.setup(sound, GPIO.IN)
GPIO.setup(motion, GPIO.IN)

#check if sound sensor is detecting sound
def detection(sound):
    if GPIO.input(sound):
        print("Sound Detected")
    else:
        print("Sound Detected")

#check if motion sensor is detecting motion
def detection(motion):
    if GPIO.input(motion):
        print("Motion Detected")
    else:
        print("Motion Detected")
        
#
GPIO.add_event_detect(sound, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(sound, detection)

#
GPIO.add_event_detect(motion, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(motion, detection)

while True:
    time.sleep(1)
