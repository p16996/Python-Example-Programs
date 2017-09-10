import turtle

t=turtle

for i in range(20):
	t.forward(i)

	t.penup()
	
	t.forward(i+1)	
	
	t.pendown()

t.exitonclick()


