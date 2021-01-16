n = int(input("Please enter a number; I'll find the square root\n> "))
guess = n / 2
while True:
	new_guess = (guess + n / guess) / 2
	if abs(guess - new_guess) < 0.01:
		guess = new_guess
		break
	guess = new_guess
print(guess)
