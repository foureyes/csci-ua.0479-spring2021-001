class Dog:
    # self will be the new instance created
    # from here, we can augment self
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        self.toys = []

    # if you want to reference a property from within your class
    # method, always prefix with self... that will refer to
    # the current instance
    def __str__(self):
        toys_string = ','.join(self.toys)
        return "A dog named " + self.name + " that has " + toys_string

    def make_noise(self):
        return self.sound.upper()

d1 = Dog('Bark Twain', 'woof')
print(d1.name)
d1.toys.extend(['chew toy', 'pig\'s ear'])
print(d1)
print(d1.make_noise())
d2 = Dog('Jane Clawsten', 'arf')
print(d2.name)
print(d2)
print(d2.make_noise())

"""
print will cause the __str__ method of an object to be called??????
"""
