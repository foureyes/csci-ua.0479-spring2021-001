"""
Demonstrates capturing keyboard input. Pressing left will make the circle move left, while pressing right will make the circle move right.

Make sure to click on window to give it focus before pressing left and right arrows.
"""
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.tracer(0)
t.hideturtle()
x, y, v = 0, 0, 2

def next_frame():
    t.clear()
    global x, v
    t.up()
    t.goto(x, y)
    t.down()
    t.circle(50)
    x += v 
    wn.ontimer(next_frame, 50)
    wn.update()


def handle_left():
    """Pressing left changes the global velocity variable to a negative value
    """
    global v
    print('left pressed')
    v = -2

def handle_right():
    """Pressing right changes the global velocity variable to a positive value
    """
    global v
    print('right pressed')
    v = 2

wn.onkeypress(handle_left, 'Left')
wn.onkeypress(handle_right, 'Right')
next_frame()
wn.listen()
wn.mainloop()
