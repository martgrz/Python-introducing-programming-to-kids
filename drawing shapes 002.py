
import turtle

t = turtle.Pen()
t.speed(0)

r = 12

n = int(turtle.numinput("Number of waves",
                   "How many waves do you want to draw (1-20)?",
                   2,1,20))


for i in range (2):
    for i in range(n):
        t.circle(r,90)
        t.circle(-r,180)
        t.circle(r,90)

    t.circle(-r,180)
   

