from tkinter import *
import RPi.GPIO as GPIO 
import time 
from picamera import PiCamera
from gpiozero import Buzzer
passwords = ["password", "123", "password123"]

class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.setupGUI()

    def setupGUI(self):
        self.pass_label = Label(window1, text = "Password")
        self.pass_label.grid(row=2, column=2)
        self.pass_entry = Entry(window1, bg = "gray")
        self.pass_entry.grid(row=2, column=3)
        self.pass_entry.bind("<Return>", self.check_pass)
        self.pass_entry.focus()

    def check_pass(self, parent):
        password = self.pass_entry.get()
        if password in passwords:
            self.settings_window()
            self.pass_entry.delete(0,END)
        else:
            incorrect = Label(window1, text="Incorrect Password")
            incorrect.grid(row=3, column=3)

    def settings_window(self):
        window2 = Toplevel(window1)
        window2.title("System Settings")
        arm_button = Button(window2, text = "Arm System", command = lambda: self.arm_sys())
        arm_button.grid(row=2, column=2)

    def arm_sys(self):
        camera = PiCamera()
        sound = 6
        motion = 4
        buzzer1 = Buzzer(22)
        buzzer2 = Buzzer(26)

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(sound, GPIO.IN)
        GPIO.setup(motion,GPIO.IN)

        def detection_sound(sound):
            if GPIO.input(sound):
                pass
            else:
                print("sound Detected")
                buzzer1.beep()
                time.sleep(5)
                buzzer1.off()

        def detection_motion(motion):
            if GPIO.input(motion):
                print("Motion Detected")
                camera.capture('/media/pi/7D10-886F/PersonSpotted.jpg')
                camera.start_recording('/media/pi/7D10-886F/PersonSpotted.h264')
                time.sleep(10)
                camera.stop_recording()
                buzzer2.on()
                time.sleep(10)
                buzzer2.off()
            else:
                pass

        GPIO.add_event_detect(sound, GPIO.BOTH, bouncetime = 300)
        GPIO.add_event_callback(sound, detection_sound)

        GPIO.add_event_detect(motion, GPIO.BOTH, bouncetime = 300)
        GPIO.add_event_callback(motion, detection_motion)

        while True:
            time.sleep(1)

window1 = Tk()
window1.title("Welcome User")
window1.geometry("1000x500")
window1 = MainGUI(window1)
window1.setupGUI
window1.mainloop()
