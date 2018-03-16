#drawing shapes 001.py

import turtle

t=turtle.Pen()
t.speed(0)
turtle.bgcolor("#00a1f1")

a = 20

t.penup()
t.setpos(-6.5*a,6.5*a) #draw the image in the centre of a window
t.pendown()
t.width(3)

t.color("white")

for j in range(4):
    t.forward(a)
    for i in range(5):
        t.forward(a)
        t.right(90)
        t.forward(a)
        t.left(90)
        t.forward(a)
        t.left(90)
        t.forward(a)
        t.right(90)

    t.forward(a*2)
    t.right(90)




