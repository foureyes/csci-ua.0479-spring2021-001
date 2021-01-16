""" Name that craps roll! (well, at least four of them)
http://en.wikipedia.org/wiki/Craps#Rolling"""

d1 = int(input("What roll did you get for the first die?\n> "))
d2 = int(input("What roll did you get for the second die?\n> "))
if d1 == 1 and d2 ==1:
    print("Snake Eyes!")
elif d1 == 1 and d2 == 3 or d1 == 3 and d2 == 1:
    print("Easy Four")
elif d1 == 2 and d2 == 2:
    print("Hard Four")
else:
    print("I don't know that roll yet")
