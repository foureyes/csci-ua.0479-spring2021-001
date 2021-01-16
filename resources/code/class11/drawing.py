from shapes import Rectangle, Circle
import turtle
t = turtle.Turtle()
t.hideturtle()
wn = turtle.Screen()
wn.tracer(0)

r = Rectangle(t, 50, 50, 100, 20)
c = Circle(t, 0, 0, 100)

def draw():
    t.clear()
    r.moveRight(5)
    r.render()
    c.moveRight(1)
    c.render()
    wn.update()
    wn.ontimer(draw, 20)

wn.ontimer(draw, 20)


wn.mainloop()
