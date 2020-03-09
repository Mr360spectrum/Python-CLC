# Karter Ence
# GUI Class
# 3/9/2020
from tkinter import *
import random
import time

class Application(Frame):
    """A GUI application with three buttons."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttnClicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text="You have clicked the button " + str(self.bttnClicks) + " times.")
        self.lbl.grid()
        self.bttn1 = Button(self, text="Click me!")
        self.bttn1.grid()
        self.bttn1.config(command = self.add_to_count)


        self.lbl2 = Label(self, text="Click to subtract from the click count:")
        self.lbl2.grid()
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.config(text="Subtract", command=self.subtract_from_count)

        self.lbl3 = Label(self, text="Click to reset:")
        self.lbl3.grid()
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Reset"
        self.bttn3["command"] = self.reset_count

        self.lbl4 = Label(self, text="Do NOT click this button.")
        self.lbl4.grid()
        self.bttn4 = Button(self, text="Seriously, do NOT click me.", command=self.mystery_button)
        self.bttn4.grid()

    def add_to_count(self):
        """Increase the click count and display the new total."""
        self.bttnClicks += 1
        self.lbl.config(text="You have clicked the button " + str(self.bttnClicks)+ " times.")
        if self.bttnClicks >= 0:
            self.lbl.config(bg="green")
        else:
            self.lbl.config(bg="red")

    def subtract_from_count(self):
        """Decrease the click count and display the new total."""
        self.bttnClicks -= 1
        self.lbl.config(text="You have clicked the button " + str(self.bttnClicks)+ " times.")
        if self.bttnClicks >= 0:
            self.lbl.config(bg="green")
        else:
            self.lbl.config(bg="red")

    def reset_count(self):
        """Reset the click count and display it."""
        self.bttnClicks = 0
        self.lbl.config(text="You have clicked the button " + str(self.bttnClicks)+ " times.")
        if self.bttnClicks >= 0:
            self.lbl.config(bg="green")
        else:
            self.lbl.config(bg="red")

    def mystery_button(self):
        """A mystery method."""
        self.lbl.config(text="huevo", bg="red", fg="green")
        self.bttn1.config(text="huevo", bg="red", fg="green")
        self.lbl2.config(text="huevo", bg="red", fg="green")
        self.bttn2.config(text="huevo", bg="red", fg="green")
        self.lbl3.config(text="huevo", bg="red", fg="green")
        self.bttn3.config(text="huevo", bg="red", fg="green")
        self.lbl4.config(text="huevo", bg="red", fg="green")
        self.bttn4.config(text="huevo", bg="red", fg="green")

        ref_x = 0
        ref_y = 0
        self.lbl.place(x=ref_x + random.randint(0, 100), y=ref_y + random.randint(0, 100))
        self.bttn1.place(x=ref_x + random.randint(0, 100), y=ref_y + random.randint(0, 100))
        self.lbl2.place(x=ref_x + random.randint(0, 100), y=ref_y + random.randint(0, 100))
        self.bttn2.place(x=ref_x + random.randint(0, 100), y=ref_y + random.randint(0, 100))
        self.lbl3.place(x=ref_x + random.randint(0, 100), y=ref_y + random.randint(0, 100))
        self.bttn3.place(x=ref_x + random.randint(0, 100), y=ref_y + random.randint(0, 100))
        self.lbl4.place(x=ref_x + random.randint(0, 100), y=ref_y + random.randint(0, 100))
        self.bttn4.place(x=ref_x + random.randint(0, 100), y=ref_y + random.randint(0, 100))
        self.after(50, self.mystery_button)

def main():
    root = Tk()
    root.title("Buttons 2.0")
    root.geometry("300x300")
    app = Application(root)
    root.mainloop()

main()
