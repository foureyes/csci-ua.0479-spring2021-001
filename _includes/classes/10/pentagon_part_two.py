import turtle
wn = turtle.Screen()
t = turtle.Turtle()

t.color('blue')
for i in range(5):
	t.forward(50)
	t.left(72)
t.up()
t.back(100)
t.down()
for i in range(5):
	t.forward(50)
	t.left(72)

wn.mainloop()

