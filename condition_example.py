import turtle

condition = True
if condition:
    print("condition met")

if not condition:
    print("condition not met")

direction = -30
if direction > 0 :
    turtle.forward(direction)
else:
    turtle.left(180)
    turtle.forward(-direction)

def move():
    direction = raw_input("Go left or right? ")
    direction = direction.strip().lower()
    if direction == "left":
        turtle.left(60)
        turtle.forward(50)
    if direction == "right":
        turtle.right(60)
        turtle.forward(50)

move()

my_variable = "       I Am Capitalised"
print(my_variable)
my_stripped = my_variable.strip()
print(my_stripped)
my_lower = my_variable.lower()
print(my_lower)

turtle.exitonclick()
