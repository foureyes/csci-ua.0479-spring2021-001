import turtle

def draw_square(t, size):
	t.down()
	for i in range(4):
		t.forward(size)
		t.left(90)	

wn = turtle.Screen()
don = turtle.Turtle()
leo = turtle.Turtle()
raph = turtle.Turtle()

leo.speed(0)

don.speed(0)
don.up()
don.goto(120, 120)
don.down()
don.color("green")

raph.speed(0)
raph.up()
raph.goto(-200, -200)
raph.down()
raph.color("blue")

for i in range(70):
	don.left(122)
	draw_square(don, 57)

	leo.right(82)
	draw_square(leo, 34)

	raph.left(10)
	draw_square(raph, 48)
	raph.up()
	raph.forward(20)
	raph.down()

wn.mainloop()
