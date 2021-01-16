import turtle

t, wn = turtle.Turtle(), turtle.Screen()

# turn animation of turtles off
t.hideturtle()
wn.tracer(0)

def draw():
	t.up()
	t.forward(5)
	t.down()
	t.circle(20)

	# update screen
	wn.update()
	
	# call again in 50 milliseconds
	wn.ontimer(draw, 50)
draw()
wn.mainloop()
