# Karter Ence
# Layouts
# 3/11/2020
from tkinter import *

root = Tk()
root.geometry("654x643")

# w = Label(root, text="Red Sun", bg="red", fg="white")
# w.pack()
# w = Label(root, text="Green Grass", bg="green", fg="black")
# w.pack()
# w = Label(root, text="Blue Sky", bg="blue", fg="white")
# w.pack()

# w = Label(root, text="Red Sun", bg="red", fg="white")
# w.pack(fill=X)
# w = Label(root, text="Green Grass", bg="green", fg="black")
# w.pack(fill=X)
# w = Label(root, text="Blue Sky", bg="blue", fg="white")
# w.pack(fill=X)

# w = Label(root, text="Red Sun", bg="red", fg="white")
# w.pack(fill=X, padx=10, pady=10)
# w = Label(root, text="Green Grass", bg="green", fg="black")
# w.pack(fill=X, padx=10, pady=10)
# w = Label(root, text="Blue Sky", bg="blue", fg="white")
# w.pack(fill=X, padx=10)

# w = Label(root, text="Red Sun", bg="red", fg="white")
# w.pack(ipadx=10)
# w = Label(root, text="Green Grass", bg="green", fg="black")
# w.pack(ipadx=10)
# w = Label(root, text="Blue Sky", bg="blue", fg="white")
# w.pack(ipady=10)

# w = Label(root, text="Red Sun", bg="red", fg="white")
# w.pack(padx=5, pady=10, side=RIGHT)
# w = Label(root, text="Green Grass", bg="green", fg="black")
# w.pack(padx=5, pady=10, side=RIGHT)
# w = Label(root, text="Blue Sky", bg="blue", fg="white")
# w.pack(padx=5, pady=10, side=RIGHT)

# frame1 = Frame(root, background="orange")
# frame1.pack(ipady=50, fill=X)
# frame2 = Frame(root, background="yellow")
# frame2.pack(side=LEFT, anchor="nw", ipady=50, ipadx=50)
# frame3 = Frame(root, background="green")
# frame3.pack(side=RIGHT, anchor="ne", ipady=50, ipadx=50)
# frame4 = Frame(root, background="red")
# frame4.pack(side=LEFT, anchor="sw", ipady=50, ipadx=50)
# frame5 = Frame(root, background="blue")
# frame5.pack(side=RIGHT, anchor="se", ipady=50, ipadx=50)

frame1 = Frame(root)
frame1.pack(fill=X)
frame2 = Frame(root)
frame2.pack(fill=X)
frame3 = Frame(root)
frame3.pack(fill=X)
frame2sub1 = Frame(frame2, background="yellow")
frame2sub1.pack(fill="both", anchor="center", ipadx=44, ipady=30, side=LEFT)
frame2sub2 = Frame(frame2, background="green")
frame2sub2.pack(fill="both", anchor="center", ipadx=50, ipady=30, side=RIGHT)
frame3sub1 = Frame(frame3, background = "red")
frame3sub1.pack(fill="both", anchor="center", ipadx=50, ipady=30, side=LEFT)
frame3sub2 = Frame(frame3, background="blue")
frame3sub2.pack(fill="both", anchor="center", ipadx=39, ipady=30, side=RIGHT)

lbl1 = Label(frame1, text="A game")
lbl1.pack(padx=100, pady=45)
bttn1 = Button(frame2sub1, text="game")
bttn1.pack(padx=100, pady=90)
bttn2 = Button(frame2sub2, text="no")
bttn2.pack(padx=100, pady=90)
bttn3 = Button(frame3sub1, text="yes")
bttn3.pack(padx=101, pady=90)
bttn4 = Button(frame3sub2, text="maybe")
bttn4.pack(padx=100, pady=90)

root.mainloop()
