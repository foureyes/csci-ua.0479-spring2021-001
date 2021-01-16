import turtle

t, wn = turtle.Turtle(), turtle.Screen()

# turn animation of turtles off
t.hideturtle()
wn.tracer(0)

for i in range(100):
	t.forward(i*2)
	t.left(45)

wn.mainloop()

