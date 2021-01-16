def factorial(n):
	product = 1
	for i in range(n, 0, -1):
		product = product * i
	return product

user_input = input("Give me a number, I'll give you the factorial\n>")
num = int(user_input)
print(factorial(num))
