#import libraries
from tkinter import *
import RPi.GPIO as GPIO 
import time 
from picamera import PiCamera
from gpiozero import Buzzer

#create a list of acceptable passwords
passwords = ["password", "123", "password123"]

#create the GUI class
class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.setupGUI()

    #set up the first window of the GUI
    def setupGUI(self):
        #have a password label and entry box
        self.pass_label = Label(window1, text = "Password")
        self.pass_label.grid(row=2, column=2)
        self.pass_entry = Entry(window1, bg = "gray")
        self.pass_entry.grid(row=2, column=3)
        self.pass_entry.bind("<Return>", self.check_pass)
        self.pass_entry.focus()

    #check to make sure password is in the list of passwords
    def check_pass(self, parent):
        password = self.pass_entry.get()
        if password in passwords:
            self.settings_window()
            #delete the entry box
            self.pass_entry.delete(0,END)
        else:
            #delete the entry box
            self.pass_entry.delete(0,END)

    #create the second window that has a button to arm the system
    def settings_window(self):
        window2 = Toplevel(window1)
        window2.title("System Settings")
        arm_button = Button(window2, text = "Arm System", command = lambda: self.arm_sys())
        arm_button.grid(row=2, column=2)

    #function to run the security program when the arm button is clicked
    def arm_sys(self):
        #labek all sensor inputs
        sound = 6
        motion = 4
        
        #label picamera
        camera = PiCamera()
        
        #label buzzers with gpiozero
        buzzer1 = Buzzer(22)
        buzzer2 = Buzzer(26)

        #set broadcom mode
        GPIO.setmode(GPIO.BCM)

        #set sensors as inputs
        GPIO.setup(sound, GPIO.IN)
        GPIO.setup(motion,GPIO.IN)

        #set up function to detect sound 
        def detection_sound(sound):
            #sound sensor sends a 0 when sound is detected
            if GPIO.input(sound):
                pass
            else:
                #print so user can see what was detected while the system was running
                print("Sound Detected")
                #set off beeping buzzer alarm
                buzzer1.beep()
                time.sleep(5)
                buzzer1.off()

        #set up function to detect motion
        def detection_motion(motion):
            #motion sensor sends a 1 when motion is detected
            if GPIO.input(motion):
                #print so user can see what was detected while the system was running
                print("Motion Detected")
                
                #take a picture and send to usb 
                camera.capture('/media/pi/7D10-886F/PersonSpotted.jpg')
                
                #take a 10 second video and send to usb 
                camera.start_recording('/media/pi/7D10-886F/PersonSpotted.h264')
                time.sleep(10)
                camera.stop_recording()
                
                #set off steady buzzer alarm for 10 seconds 
                buzzer2.on()
                time.sleep(10)
                buzzer2.off()
                   
            else:
                pass
    
        #add event detection and callback for sound sensor
        GPIO.add_event_detect(sound, GPIO.BOTH, bouncetime = 300)
        GPIO.add_event_callback(sound, detection_sound)

        #add event detection and callback for motion sensor
        GPIO.add_event_detect(motion, GPIO.BOTH, bouncetime = 300)
        GPIO.add_event_callback(motion, detection_motion)

        while True:
            time.sleep(1)

#set up GUI window1
window1 = Tk()
window1.title("Welcome User")
#make window almost fullscreen on pi
window1.geometry("1000x500")
window1 = MainGUI(window1)
window1.setupGUI
window1.mainloop()
