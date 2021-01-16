
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
t.hideturtle()
wn.tracer(0)
wn.setup(400, 400)

pos = [100, 100]
def draw_star(x, y, s):
    t.setheading(0)
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(5):
        t.left(144)
        t.forward(s)

wn.bgcolor('black')
t.color('yellow')
t.pensize(5)

velocity = 4

def draw():
    global velocity
    # change the y position to subtract 50
    t.clear()
    pos[1] -= velocity
    x, y = pos
    # draw star at its cur position
    draw_star(x, y, 50)

    # refresh the screen
    wn.update()
    if pos[1] <= -200:
        velocity *= -1
        #pos[1] = 210
    # 1/2 second later, run this same function again
    wn.ontimer(draw, 50)

"""
while True
    wn.ontimer(draw, 500)
"""

wn.ontimer(draw, 1000)




wn.mainloop()
