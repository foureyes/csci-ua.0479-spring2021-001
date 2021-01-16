import turtle
def draw():

	# clear all drawings
	t.clear()
	t.hideturtle()
	t.penup()
	t.goto(turtle_x[0], turtle_y[0])
	t.pendown()
	turtle_y[0] -= 1
	t.circle(15)

	# update the screen because trace is off
	# http://docs.python.org/3.3/library/turtle.html#turtle.update
	wn.update()

	# call this function again to redraw entire screen
	wn.ontimer(draw, 30)

t, wn = turtle.Turtle(), turtle.Screen()

# store x and y values in a list so that they can be changed from draw function
# (rather than use globals keyword)
turtle_x, turtle_y = [0], [0] 

# turn animation of turtles off
wn.tracer(0)

# start off our draw function!
draw()
wn.mainloop()
