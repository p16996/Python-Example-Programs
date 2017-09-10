import turtle

def hexagon(size):
    for i in range(6):
        turtle.forward(size)
        turtle.left(360/6)

for i in range(6):
    hexagon(60)
    turtle.forward(50)
    turtle.right(360/6)
    

turtle.exitonclick()
