"""Translate place number into Olympic medal.  FTW!"""

place = int(input('What number should I translate into a medal?\n>'))
if place == 1:
    medal = "gold"
elif place == 2:
    medal = "silver"
elif place == 3:
    medal = "bronze"
else:
    medal = "no medal for you!"
print(medal)
