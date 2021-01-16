def gcd(a, b):
    while a != b:
        # let's always make a the larger number
        if a < b:
            # swap the values!
            a, b = b, a
        else:
            a = a - b
    return a
print(gcd(12, 8))
print(gcd(30, 105))
