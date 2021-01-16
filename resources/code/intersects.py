"""
Colliding Rectangles
=====

The following program will:

1. Draw two rectangles
2. One rectangle moves horizontally across the screen
3. The second rectangle does not move
4. The path of the first rectangle's movement will cause it to collide
   with the second rectangle
5. When any part of of the first rectangle touches the second rectangle,
   the first rectangle's color changes

This uses a naive algorithm for determining collisions:

1. for every corner of rectangle 1
2. check if it's within rectangle 2
3. if any corner is within rectangle 2, then the rectangles have collided
"""
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
t.hideturtle()
wn.tracer(0)
WIDTH, HEIGHT = 500, 500
wn.setup(WIDTH, HEIGHT)
x, y, w, h, v = -300, 0, 50, 50, 3

def draw_rect(t, x, y, w, h, color='#7777aa'):
    t.color(color)
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(0)
    for i in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()

def point_in_rectangle(x, y, x1, y1, x2, y2):
    return x >= x1 and x <= x2 and y >= y2 and y <= y1

def next_frame():
    t.clear()
    global x
    color = '#228855'
    for p in [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]:
        if point_in_rectangle(p[0], p[1], 0, 0, 100, -100):
            color = '#881133'
    draw_rect(t, 0, 0, 100, 100)
    draw_rect(t, x, y, w, h, color=color)
    x += v
    if x > WIDTH / 2:
        x = - WIDTH / 2
    wn.ontimer(next_frame, 10)

next_frame()
wn.mainloop()
