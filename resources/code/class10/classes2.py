
class CutenessFactorError(Exception):
    pass

class Cat:
    # constructor
    def __init__(self, n, cuteness_factor):
        self.name = n
        self.cuteness_factor = cuteness_factor

    def __str__(self):
        return "the cat named " + self.name

    def meow(self, target):
        print(self.name, 'meows at', target)

    def set_cuteness_factor(self, n):
        if n <= 10 and n >= 0:
            self.cuteness_factor = n
        else:
            raise CutenessFactorError()



# objects are mutable
# you can dot properties and assign immediately
c = Cat('Paw Newman', 9)
"""
print(c.cuteness_factor)
c.cuteness_factor = 2
print(c.cuteness_factor)
c.set_cuteness_factor(100)
print(c.cuteness_factor)
"""
print(c)






