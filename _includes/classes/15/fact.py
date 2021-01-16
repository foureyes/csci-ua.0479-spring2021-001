def factorial(n):
	if n != 0:
		return n * factorial(n-1)
	else:
		return 1

print(factorial(0))
print(factorial(2))
print(factorial(3))
print(factorial(5))
