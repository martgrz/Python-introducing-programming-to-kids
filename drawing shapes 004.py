import turtle
import random

t = turtle.Pen()
t.speed(0)

t.left(90)

flowers = 8
stem = 200
petal = 50

for k in range(flowers):
    
    t.forward(stem)
    t.left(45)

    for j in range (3):
        t.color(random.random(),random.random(),random.random())
        t.begin_fill()
        for i in range(4):
            t.forward(petal)
            t.right(90)
        t.right(120)
        t.end_fill()
    t.color("green")
    t.right(45)
    t.backward(200)
    t.right(360/flowers)



