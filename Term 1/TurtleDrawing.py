import turtle
import random as rand
import time

turtle.bgcolor("black")
bob = turtle.Pen()
bob.shape("turtle")
bob.color("purple")
bob.speed(100)

# bob.forward(100)
# bob.left(90)
# bob.right(180)
# bob.backward(100)
# bob.circle(100)
# bob.speed(0)
# bob.width(27)
# bob.up()
# bob.down()

# for i in range(4):
#     bob.forward(100)
#     bob.left(90)

# joe = turtle.Pen()
# joe.shape("turtle")
# joe.color("red")
# joe.forward(200)

# bob.right(72)
# bob.forward(100)
# bob.left(144)
# bob.forward(100)
# bob.left(144)
# bob.forward(100)
# bob.left(144)
# bob.forward(100)
# bob.left(144)
# bob.forward(100)

# for i in range(200):
#     bob.forward(i)
#     bob.right(i * 2)

colors = ("red", "blue", "green", "yellow", "purple")
bob.setposition(x=0, y=0)
for turn in range(3):
    bob.right(turn * 90)
    for i in range(200):
        bob.speed(100)
        fillCircle = rand.randint(0,5)
        if fillCircle == 5:
            bob.begin_fill()
            bob.circle(i)
            bob.end_fill()
        else:
            bob.circle(i)
        bob.left(10)
        bob.forward(i * 5)
        bob.right(470)
        randColor = rand.choice(colors)
        bob.color(randColor)
    bob.penup()
    bob.setposition(x=0, y=0)
    bob.right(turn * 180)
    bob.pendown()
bob.penup()
bob.speed(9)
bob.goto(x=-500, y=-200)
time.sleep(3)
bob.write("yeet", font=("Comic Sans MS", 380, "normal"))

# for i in range(100):
#     bob.forward(i)
#     bob.circle(i*2, 90)
#     bob.right(97)

# for i in range(180):
#     bob.forward(100)
#     bob.right(30)
#     bob.forward(20)
#     bob.left(60)
#     bob.forward(50)
#     bob.right(30)

#     bob.penup()
#     bob.setposition(0, 0)
#     bob.pendown()
    
# for i in range(100):
#     bob.forward(20)
#     bob.right(i*-20)
#     bob.forward(50)
#     bob.right(i*-20)
#     bob.circle(27)
#     bob.write("yeet")
#     bob.forward(20)
#     bob.right(i*-20)
#     bob.circle(27)
#     bob.write("yeet")


# Stops the window from immediately closing when the drawing is complete
preventClose = input()