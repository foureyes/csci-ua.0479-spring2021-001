print('square root calculator...')
n = int(input('enter a number\n> '))
guess = n / 2
threshold = 0.0001
while True:
    # approximate
    new_guess = (guess + n / guess) / 2

    # compare new approximation to old...
    if abs(new_guess - guess) < threshold: 
        guess = new_guess
        break
    guess = new_guess
print(guess)
