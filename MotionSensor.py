import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD)

try:
    print("Test")
    time.sleep(2)
    print("Ready")

    while True:
        if GPIO.input(24) == GPIO.HIGH:
            print("Motion detected")
        time.sleep(2)

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
