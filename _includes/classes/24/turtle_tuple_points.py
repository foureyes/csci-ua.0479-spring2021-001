import turtle
t = turtle.Turtle()
wn = turtle.Screen()
for x, y in [(0,50),(50,50),(50,0),(0,0)]:
	t.goto(x, y)
wn.mainloop()
