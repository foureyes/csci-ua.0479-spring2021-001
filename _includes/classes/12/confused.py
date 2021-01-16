import turtle
import random
wn = turtle.Screen()
t = turtle.Turtle()

t.color("blue")
for i in range(50):
	t.pensize(random.randint(1, 12))
	t.goto(random.randint(-300, 300), random.randint(-200, 200))
	if i == 25:
		# change the color once to green
		t.color("purple") 

wn.mainloop()
