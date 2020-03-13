# Karter Ence
# Layouts 3 (Place)
# 3/13/2020
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text="Enter password to get access to the Meaning of Life.")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        self.lblPW = Label(self, text="Password:")
        self.lblPW.grid(row=1, column=0, sticky=W)
        
        self.password = Entry(self)
        self.password.grid(row=1, column=1, columnspan=2)

        self.submitBttn = Button(self, text="Submit", command=self.reveal)
        self.submitBttn.grid(row=2, column=0, columnspan=2)

        self.replyText = Text(self, width=35, height=20, wrap=WORD)
        self.replyText.grid(row=3, column=0, columnspan=2)

        self.movieLbl = Label(self, text="What's your favorite genre of movie?")
        self.movieLbl.grid(row=2)

    def reveal(self):
        enterPW = self.password.get()
        if enterPW == "password":
            message = "The Meaning of Life is:\n \t\t\t\t\t >>> null exception error <<<"
        else:
            message = "GONTRALURATIONS! \nYou don't deserve to know."
        
        self.replyText.delete(0.0, END)
        self.replyText.insert(0.0, message)

def main():
    root = Tk()
    root.title("Password.exe")
    app = Application(root)
    root.mainloop()

main()
