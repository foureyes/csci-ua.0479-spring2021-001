import turtle

def draw():
	t.clear()
	t.hideturtle()
	t.penup()
	t.goto(turtle_x[0], turtle_y[0])
	t.pendown()
	turtle_y[0] += turtle_dy[0]

	# change velocity based on acceleration
	turtle_dy[0] += acc
	t.circle(15)

	wn.update()

	wn.ontimer(draw, 30)
	
	# bounce!
	if turtle_y[0] <= -250:
		turtle_dy[0] *= -1

t, wn = turtle.Turtle(), turtle.Screen()

turtle_x, turtle_y, turtle_dx, turtle_dy = [0], [0], [0], [-0.1]

# store acceleration
acc = -0.5

# turn animation of turtles off
wn.tracer(0)
draw()
wn.mainloop()
