import random

password_length = 1
while password_length != 0:
	password_length = int(input('Please enter a pasword length (0 to exit)\n>'))
	password = ''
	for i in range(password_length):
		password += str(random.randint(0, 9))
	print(password)
