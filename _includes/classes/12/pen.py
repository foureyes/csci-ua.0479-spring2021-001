import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.pensize(5)

t.left(90)
t.forward(40)
t.up()             # don't draw
t.forward(20)
t.down()           # draw
t.forward(40)
t.up()             # don't draw
t.forward(20)
t.down()           # draw
t.forward(40)

wn.mainloop()
