"""
from matplotlib import pyplot as plt
plt.figure(1)
plt.subplot(211)
plt.plot([1,0. 2,0. 3,0. 4],0. [4,0. 7,0. 8,0. 9])
#plt.figure(2)
plt.subplot(212)
plt.hist([1,0. 3,0. 7,0. 4,0. 2])
plt.show()
"""
"""
import matplotlib.pyplot as plt

scores = [0.82, 0.88, 0.96, 0.90, 0.87, 0.88, 0.81, 0.90, 0.90, 0.74, 0.82, 0.73, 0.92, 0.76, 0.87, 0.90, 0.90, 0.74, 0.72, 0.88, 0.62, 0.70, 0.82, 0.82, 0.90, 0.74, 0.65, 0.86, 0.89, 0.97, 0.46, 0.89, 0.82, 0.87, 0.90, 0.96, 0.92, 0.60, 0.91, 0.26, 0.92, 0.91, 0.60, 0.94, 0.87, 0.91, 0.92, 0.98, 0.96, 0.96, 0.96, 0.81, 0.67, 0.81, 0.91, 0.94, 0.94, 0.96, 0.95, 0.90]
bins = [0.6, 0.7, 0.73, 0.77, 0.8, 0.83, 0.87, 0.9, 0.93, 1]
plt.hist(scores, bins)
plt.xticks(bins, ['F', 'D', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A'])
plt.show()
"""
"""
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    @staticmethod
    def gcf(a, b):
        if a > b:
            b, a = a, b
        gcf = 1
        for factor in range(1, a + 1):
            if a % factor == 0 and b % factor == 0:
                gcf = factor
        return gcf

    def reduce(self):
        factor = Fraction.gcf(self.num, self.den)
        new_num = self.num // factor
        new_den = self.den // factor
        return Fraction(new_num, new_den)

    def add(self, other):
        new_num = (other.den * self.num) + (other.num * self.den)
        new_den = other.den * self.den 
        result = Fraction(new_num, new_den)
        return result.reduce()

    def __add__(self, other):
        return self.add(other)

    def __gt__(self, other):
        self_num = self.num * other.den
        other_num = other.num * self.den
        return self_num > other_num

    def __lt__(self, other):
        self_num = self.num * other.den
        other_num = other.num * self.den
        return self_num < other_num

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __repr__(self):
        return self.__str__()
        
def silly(fn):
    def new_fn(*args):
        print('start')
        result = fn(*args)
        print('end')
        return result
    return new_fn


@silly
def foo(a, b):
    return a + b

print(foo(2, 3))


a = Fraction(1, 2)
print(a)
print(Fraction.gcf(4, 8))
print(Fraction.gcf(9, 6))
print(Fraction.gcf(17, 5))

b = Fraction(2, 8)
print(a.add(b))

print(a + b)
a.foozy = 'barry'
print(a.foozy)
b.num = 6
print(b)
#print(b.foozy)
print(type(b))

print(a > b)
print(b > a)
c = Fraction(1,3)


print('c < a', c < a)
print('c < b', c < b)
print('c == c', c == c)
print('c != c', c != c)

fractions = [a, b, c]
fractions.sort()
print(fractions)

print([range(4), range(2)])
"""     


"""
class Rectangle: 
    def __init__(self, t, x, y, w, h, color):
        self.t = t
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def area(self):
        return self.w * self.h

    def __lt__(self, other):
        return self.area() < other.area

    def __str__(self):
        return "{} x {} at ({}, {})".format(self.w, self.h, self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.w == other.w and self.h == other.h

    def render(self):
        self.t.up()
        self.t.color = self.color
        self.t.begin_fill()
        self.t.goto(self.x, self.y)
        self.t.down()
        self.t.goto(self.x + self.w, self.y)
        self.t.goto(self.x + self.w, self.y - self.h)
        self.t.goto(self.x, self.y - self.h)
        self.t.goto(self.x, self.y)
        self.t.end_fill()





import turtle
t = turtle.Turtle()
t.hideturtle()
wn = turtle.Screen()
wn.tracer(0)

r1 = Rectangle(t, 50, 50, 100, 50, 'black')
r2 = Rectangle(t, -50, -50, 100, 100, 'red')
def draw():
    t.clear()
    r1.x += 1
    r1.render()
    r2.render()
    wn.ontimer(draw, 20)

wn.ontimer(draw, 200)
wn.update()
wn.mainloop()
"""

"""
class Sprite:
    def __init__(self, t, x, y):
        self.t = t
        self.x = x
        self.y = y

    def move_right(self, delta):
        self.x += delta

    def render(self):
        self.t.up()
        self.t.goto(self.x, self.y)
        self.t.down()

class Circle(Sprite):
    def __init__(self, t, x, y, r):
        super().__init__(t, x, y)
        self.r = r

    def render(self):
        super().render()
        self.t.circle(self.r)



class Rectangle(Sprite):
    def __init__(self, t, x, y, w, h, color):
        super().__init__(t, x, y)
        self.w = w
        self.h = h
        self.color = color

    def area(self):
        return self.w * self.h

    def __lt__(self, other):
        return self.area() < other.area

    def __str__(self):
        return "{} x {} at ({}, {})".format(self.w, self.h, self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.w == other.w and self.h == other.h

    def render(self):
        super().render()
        self.t.color = self.color
        self.t.begin_fill()
        self.t.goto(self.x + self.w, self.y)
        self.t.goto(self.x + self.w, self.y - self.h)
        self.t.goto(self.x, self.y - self.h)
        self.t.goto(self.x, self.y)
        self.t.end_fill()





import turtle
t = turtle.Turtle()
t.hideturtle()
wn = turtle.Screen()
wn.tracer(0)

r1 = Rectangle(t, 50, 50, 100, 50, 'black')
r2 = Rectangle(t, -50, -50, 100, 100, 'red')
c = Circle(t, 0, 100, 100)
def draw():
    t.clear()
    r1.move_right(5)   
    c.move_right(3)
    r1.render()
    r2.render()
    c.render()
    wn.update()
    wn.ontimer(draw, 20)

wn.ontimer(draw, 200)
wn.mainloop()
"""

#from matplotlib import pyplot as plt
"""
plt.plot([1, 2, 3, 4, 5], [2, 4, 1, 1, 5])
plt.xlim(0, 10)
plt.ylim(0, 10)
"""
#plt.bar(['lemons', 'apples', 'oranges', 'limes'], [5, 12, 2, 3])
#plt.hist([1,0. 3,0. 7,0. 4,0. 2])
#plt.show()
import matplotlib.pyplot as plt

data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
names = list(range(1, len(data.keys()) + 1))
values = list(data.values())


plt.bar(names, values)
plt.xticks(names, list(data.keys()))
#plt.xticklabels(list(data.keys()))
plt.show()
