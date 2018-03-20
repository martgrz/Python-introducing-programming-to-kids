import turtle
import random

t = turtle.Pen()
t.speed(0)
t.width(2)

r = 15
n = 7


for i in range (2):
    for i in range(n):
        
        t.color(random.random(),random.random(),random.random())
        t.circle(r,90)

        t.color(random.random(),random.random(),random.random())
        t.circle(-r,90)

        t.color(random.random(),random.random(),random.random())
        t.circle(-r,90)

        t.color(random.random(),random.random(),random.random())
        t.circle(r,90)
        

    t.color(random.random(),random.random(),random.random())    
    t.circle(-r,90)

    t.color(random.random(),random.random(),random.random())    
    t.circle(-r,90)
    
   

