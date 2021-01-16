class Fraction:


    def __init__(self, n, d):
        self.n = n
        self.d = d
    # this means that this method can be called without instance
    # and consequently, no self is needed
    # instead, you call it on the actual class itself
    # Fraction.gcf()
    @staticmethod 
    def gcf(a, b):
        # go through every possible factor
        # check if it divides evenly into both
        # return the largest one
        cur_gcf = 1
        for factor in range(1, a + 1):
            if a % factor == 0 and b % factor == 0:
                cur_gcf = factor
        return cur_gcf

    def reduce(self):
        gcf = Fraction.gcf(self.n, self.d)
        return Fraction(self.n // gcf, self.d // gcf)

    def __str__(self):
        return "{}/{}".format(self.n, self.d)

    def __repr__(self):
        # we can call methods that already defined
        return self.__str__()

    def add(self, other):
        new_n = (self.n * other.d) + (other.n * self.d)
        new_d = self.d * other.d
        return Fraction(new_n, new_d)

    def __add__(self, other):
        return self.add(other)

    def __eq__(self, other):
        return self.n == other.n and self.d == other.d

a = Fraction(1, 2)
b = Fraction(6, 8)
c = Fraction(1, 3)
fractions = [a, b, c]
print(fractions)
print(a.add(c))
print(a + c)
print(a == c)
print(a == Fraction(1, 2))
print(Fraction.gcf(9, 12))
print(Fraction(4, 8).reduce())











