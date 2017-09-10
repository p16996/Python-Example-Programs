import turtle

def draw_shape(sides,length):
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(360/sides)

def gap():	
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()

draw_shape(3,40)
gap()
draw_shape(4,40)
gap()
draw_shape(5,40)
gap()
draw_shape(6,40)


turtle.exitonclick()
