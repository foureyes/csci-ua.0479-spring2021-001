import turtle

leo = turtle.Turtle()
wn = turtle.Screen()
def branch(t, length, length_multiplier, min_length):
	if length < min_length:
		return
	else:
		t.forward(length)
		t.left(30)
		branch(t, length * length_multiplier, length_multiplier, min_length)
		t.right(60)
		branch(t, length * length_multiplier, length_multiplier, min_length)
		t.left(30)
		t.back(length)
		return
# base - branch(leo, , 0.6, 10)
branch(leo, 80, 0.6, 10)
wn.mainloop()
