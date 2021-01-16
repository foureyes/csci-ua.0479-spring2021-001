class Shape:
    def __init__(self, pencil, x, y):
        self.pencil = pencil
        self.x = x
        self.y = y

    def moveRight(self, delta):
        self.x += delta

    def render(self):
        self.pencil.up()
        self.pencil.goto(self.x, self.y)
        self.pencil.down()

class Circle(Shape):
    def __init__(self, pencil, x, y, r):
        super().__init__(pencil, x, y)
        self.r = r

    def render(self):
        super().render()
        self.pencil.circle(self.r)


class Rectangle(Shape):
    def __init__(self, pencil, x, y, w, h):
        super().__init__(pencil, x, y)
        self.w = w
        self.h = h

    def render(self):
        super().render()
        self.pencil.goto(self.x + self.w, self.y)
        self.pencil.goto(self.x + self.w, self.y + self.h)
        self.pencil.goto(self.x, self.y + self.h)
        self.pencil.goto(self.x, self.y)







    
