import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    print("Test")
    time.sleep(2)
    print("Ready")

    while True:
        if GPIO.input(4) == GPIO.HIGH:
            print("Sound detected")
        time.sleep(2)

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
