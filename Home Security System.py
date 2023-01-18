from tkinter import *
class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.attributes("-fullscreen", True)
        self.setupGUI()
    def setupGUI(self):
        self.display = Label(self, text="", anchor=E,\
         bg="white", height=2, font=("TexGyreAdventor", 50))
        
        self.display.grid(row=0, column=0, columnspan=4,\
         sticky=E+W+N+S)
        for row in range(6):
            Grid.rowconfigure(self, row, weight=1)
           
        for col in range(4):
            Grid.columnconfigure(self, col, weight=1)

        



window = Tk()
window.title("Welcome User")
r = MainGUI(window)
window.mainloop()


pass_label = Tk.Label(window, text = "Password", font = ("calibre", 14,"bold"))
pass_entry = Tk.Entry(window, textvariable = pass_var, font = ("calibre", 14, "normal"), show = "*")
