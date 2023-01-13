from tkinter import *
class MainGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        master.attributes("-fullscreen", True)
        self.setupGUI()
    
    def pWindow(self):
        homeWindow = tkinter.Tk()
        homeWindow.title("Home Alert System")
        e1 =tkinter.Entry(homeWindow)

window = Tk()
window.title("Welcome User")
r = MainGui(window)
window.mainloop()
