import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from gpiozero import Buzzer

try:
    #set up picamera
    camera = PiCamera()

    #set sound as the GPIO pin the sound sensor is connected to
    sound = 6

    #set motion as the GPIO pin the motion sensor is connected to
    motion = 4

    #set up buzzer
    buzzer1 = Buzzer(23)
    buzzer2 = Buzzer(26)

    #set the GPIO to broadcom mode
    GPIO.setmode(GPIO.BCM)

    #set the pins as inputs
    GPIO.setup(sound, GPIO.IN)
    GPIO.setup(motion, GPIO.IN)

    #check if sound sensor is detecting sound
    def detection_sound(sound):
        if GPIO.input(sound):
            print("Sound Detected")
            buzzer1.beep()
        else:
            print("Sound Detected")

    #check if motion sensor is detecting motion
    def detection_motion(motion):
        if GPIO.input(motion):
            print("Motion Detected")
            #take picture when motion is detected
            camera.capture('/home/pi/Desktop/PersonSpotted.jpg')
            buzzer2.on()
        else:
            pass

    #
    GPIO.add_event_detect(sound, GPIO.BOTH, bouncetime = 300)
    GPIO.add_event_callback(sound, detection_sound)

    #
    GPIO.add_event_detect(motion, GPIO.BOTH, bouncetime = 300)
    GPIO.add_event_callback(motion, detection_motion)

    while True:
        time.sleep(1)
        
 except KeyboardInterrupt:
    GPIO.cleanup()
