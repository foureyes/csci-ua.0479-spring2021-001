"""Ask me if I want cake, I *dare* you to."""
answer = input("Do you want cake?\n> ")
if answer == 'yes' or answer == 'yeah':
    print("Here, have some cake.")
elif answer == 'no':
    print("No cake for you.")
elif answer == 'maybe':
    print("So, call me.")
else:
    print("I do not understand.")
