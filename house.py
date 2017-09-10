import turtle
import math

a=50
b=50
c=math.sqrt(a**2+b**2)

t=turtle

t.forward(a)
t.left(90)
t.forward(b)
t.right(45)
t.backward(c)
t.left(45)
t.forward(b)
t.right(90)
t.forward(a)
t.left(120)
t.forward(a)
t.left(120)
t.forward(a)
t.right(105)
t.backward(c)

t.exitonclick()
