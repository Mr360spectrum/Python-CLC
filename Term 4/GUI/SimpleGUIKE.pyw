# Karter Ence
# Simple GUI
# 3/5/2020
from tkinter import *

root = Tk()

root.title("Simple GUI with Label and Buttons")
root.geometry("2000x500")
root.config(bg="#ea4fff")

app = Frame(root)
app.config(bg="#c75858")
app.grid()

lbl = Label(app, text="Why are you like this?", font=("Wingdings", 16))
lbl.config(bg="#edd51f", fg="orange")
lbl.grid()

lbl = Label(app, text="The FitnessGram™ Pacer Test is a \nmultistage aerobic capacity test that progressively g\nets more difficult as it continues. The 20 meter pacer test wi\nll begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets f\naster each minute after you hear this signal. [beep] A single lap should be completed each ti\nme you hear this sound. [ding] Remember to run in a straight line, and run \nas long as possible. The second time you fail to complete a lap before the sound, your test is ov\ner. The test will begin on the word start. On y\nour mark, get ready, start.", font=("ComicSans", 21))
lbl.config(bg="green", fg="red")
lbl.grid()

for i in range(7):
    bttn = Button(app, text = "que huevo?")
    bttn.config(bg = "#77f2ae", fg="yellow")
    bttn.grid()

root.mainloop()
