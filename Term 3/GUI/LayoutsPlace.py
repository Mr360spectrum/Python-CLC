# Karter Ence
# Layouts 3 (Place)
# 3/13/2020
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.place()
        self.create_widgets()

    def create_widgets(self):
        pass


def main():
    root = Tk()
    root.geometry("400x400")
    root.title("Password.exe")
    lbl = Label(text="Enter password to get access to the Meaning of Life.", bg="green")
    lbl.place(x=50, y=50, width=400, height=25)
    root.mainloop()

main()
