def factorial(n):
	product = 1
	for i in range(n, 0, -1):
		product = product * i
	return product

print(factorial(4))
print(factorial(20))
