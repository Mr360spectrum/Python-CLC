# Karter Ence
# Layouts 2
# 3/11/2020
from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("program.exe")

top = Frame(root, bg="red", height=100, width=500)
top.pack(fill=X)
lbl = Label(top, text="Label")
lbl.pack(padx=40, pady=40)
mid = Frame(root, bg="green", height=150, width=500)
mid.pack()
midLeft = Frame(mid, bg="yellow", height=150, width=250)
midLeft.pack(side=LEFT)
midLeftBttn = Button(midLeft, text="Button")
midLeftBttn.pack(fill=BOTH, padx=102, pady=102)
midRight = Frame(mid, bg="green", height=150, width=250)
midRight.pack(side=RIGHT)
midRightBttn = Button(midRight, text="Button")
midRightBttn.pack(fill=BOTH, padx=102, pady=102)
bot = Frame(root, bg="blue", height=150, width=500)
bot.pack()
botLeft = Frame(bot, bg="red", height=150, width=250)
botLeft.pack(side=LEFT)
botLeftBttn = Button(botLeft, text="Button")
botLeftBttn.pack(fill=BOTH, padx=102, pady=102)
botRight = Frame(bot, bg="blue", height=150, width=250)
botRight.pack(side=RIGHT)
botRightBttn = Button(botRight, text="Button")
botRightBttn.pack(fill=BOTH, padx=102, pady=102)

root.mainloop()