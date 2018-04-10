import turtle

t = turtle.Pen()
t.speed(0)

turtle.bgcolor("green")
t.pencolor("white")
t.width(10)

def up():
    t.forward(20)

def left():
    t.left(90)
    t.forward(20)

def right():
    t.right(90)
    t.forward(20)


turtle.onkeypress(up,"Up")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")

turtle.listen(up,"Up")


