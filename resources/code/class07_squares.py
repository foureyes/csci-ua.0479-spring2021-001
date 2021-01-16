import turtle
t = turtle.Turtle()
wn = turtle.Screen()
t.hideturtle()
wn.tracer(0)

def polygon(x, y, size, sides):
    angle = 360 / sides
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(sides):
        t.forward(size)
        t.left(angle)

def pentagon(x, y, size):
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(5):
        t.forward(size)
        t.left(72)

def square(x, y, size):
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(4):
        t.forward(size)
        t.left(90)
def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

"""
for i in range(3, 100):
    polygon(0, 0, 50, i)
"""
"""
for i in range(1000):
    t.left(15)
    square(i * 2, 0, 100)

"""
#pentagon(0, 0, 100)
#  usual turtle set up above is omitted

#  assuming draw_square function was defined above
"""
def draw_stuff():
    draw_square(20)
    t.up()
    t.forward(22)
    t.down()
    wn.update()
"""
def draw_stuff():
    # clear the screen
    t.clear()
    draw_square(20)
    t.up()

    # descrease the forward movement 
    t.forward(2)
    t.down()
    wn.update()
    wn.ontimer(draw_stuff, 60)

wn.ontimer(draw_stuff, 50)
wn.mainloop()




wn.update()

wn.mainloop()
