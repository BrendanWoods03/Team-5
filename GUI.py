from tkinter import *

#list of possible passwords (do we need to create a window for them to
#create their password? if we do how do we keep it from popping up every time?
passwords = ["password", "123", "password123"]

class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.setupGUI()

    #sets up the GUI    
    def setupGUI(self):
        self.pass_label = Label(window1, text = "Password")
        self.pass_label.grid(row = 2, column = 2)
        self.pass_entry = Entry(window1, bg = "gray")
        self.pass_entry.grid(row = 2, column = 3)
        self.pass_entry.bind("<Return>", self.check_pass)
        self.pass_entry.focus()

    #check the password to see to open a new window
    def check_pass(self, parent):
        password = self.pass_entry.get()
        if password in passwords:
            self.settings_window()

        #if the password is wrong, tell the user 
        else:
            incorrect = Label(window1, text = "Incorrect Password")     #this does not work atm
            incorrect.grid(row = 3, column = 3)

    #create second window
    def settings_window(self):
        #create window
        window2 = Toplevel(window1)

        #name window
        window2.title("System Settings")
        
        #create arm button
        arm_button = Button(window2, text = "Arm System", command = self.arm_sys())
        arm_button.grid(row = 2, column = 2)

        #create disarm button
        disarm_button = Button(window2, text = "Disarm System", command = self.disarm_sys())
        disarm_button.grid(row = 2, column = 3)
        
    #function that turns the security system on 
    def arm_sys(self):
        pass #create command later

    #function that turns the system off
    def disarm_sys(self):
        pass #create command later

#create the window
window1 = Tk()

#name the window
window1.title("Welcome User")

#display the window
window1 = MainGUI(window1)
window1.setupGUI
window1.mainloop()
