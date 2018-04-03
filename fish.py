import turtle

t = turtle.Pen()
t.speed(0)

t.penup()
t.setpos(0,150)
t.pendown()

columns = 7
rows = 7
a = 50

for row in range(rows):
    for col in range(columns):
        for i in range(4):
            t.forward(a)
            t.right(90)
            
        t.penup()
        t.forward(a)
        t.pendown()
    t.backward(a*columns)
    t.right(90)
    t.forward(a)
    t.left(90)

t.color("#00a1f1")
t.pensize(5)

t.penup()
t.home()
t.pendown()



t.left(90)
t.circle(-2*a,90)

t.left(90)
t.circle(-a,90)

t.right(90)
t.forward(a)
t.right(90)
t.circle(a,-90)

t.left(180)
t.circle(a,180)
t.circle(-a,90)

t.right(90)
t.forward(1.5*a)

t.circle(-a,90)

t.circle(a,-90)
t.backward(1.5*a)

t.left(90)
t.circle(-a,90)

t.circle(a,180)

t.circle(-a,90)

t.left(90)
t.forward(a)
t.right(90)
t.circle(-a,90)

t.right(90)
t.circle(2*a,-90)

t.left(90)
t.forward(a)

t.left(90)
t.circle(a,90)

t.penup()
t.setpos(2*a,a)
t.pendown()

t.circle(a/2)

turtle.exitonclick()
