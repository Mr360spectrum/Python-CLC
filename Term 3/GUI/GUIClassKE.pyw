# Karter Ence
# GUI Class
# 3/9/2020
from tkinter import *

class Application(Frame):
    """A GUI application with three buttons."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        lbl = Label(text="This is button 1")
        lbl.grid()
        self.bttn1 = Button(self, text="que huevo?").grid()

        Label(self, text="This is button 2").grid()
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.config(text="no")

        Label(self, text="This is button 3").grid()
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "ur mom lol hhehehehehehheheeehehehe"

def main():
    root = Tk()
    root.title("Buttons 2.0")
    root.geometry("720x1080")
    app = Application(root)
    root.mainloop()

main()