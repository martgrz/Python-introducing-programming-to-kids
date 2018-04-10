import turtle

t = turtle.Pen()

turtle.bgcolor("blue")
t.pencolor("white")

t.speed(0)
t.width(20)

turtle.onscreenclick(t.setpos)
