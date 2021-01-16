

"""
t = turtle.Turtle()

c = Cat()
"""



"""
type = a category of values
class = same as type...: Cat
the thing that we use as a "blueprint" for creating objects of a specific type

instance is the actual object that's created from a class (the instantiation of a class): c

method = some action or function that you can call on an instance: meow
constructor = is the function that gets called when you create a new object of that class: __init__
property = a piece of data on an instance: name, cuteness factor
"""
"""
imperetive 
object oriented
create classes

meta class programming ... <--

functional programming ... functions and higher order functions to tackle a problem
"""

"""
class Cat:
    # constructor
    def __init__(self, n, cuteness_factor):
        self.name = n
        self.cuteness_factor = cuteness_factor

    def meow(self, target):
        print(self.name, 'meows at', target)


c = Cat('Paw Newman', 9)
c.meow('fish')
c2 = Cat('Kitty Purry', 9)
"""



"""
c = Cat('Paw Newman', 9)
print(c.name)
print(c.cuteness_factor)
print(c)
print(type(c))
"""

"""
def foo(s):
    print(s + '!')

def call_twice(f): # higher order function
    f('hello')
    f('hello')


call_twice(foo)
"""

"""
# function that returns another function
def make_adder(base):

    def new_func(n):
        return base + n

    return new_func


addFive = make_adder(5)
addThree = make_adder(3)

print(addFive(1))
print(addThree(1))
"""

























