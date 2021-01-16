def fact(n):
	result = 1
	while n > 0: 
		result *= n 
		n -= 1
	return result

print(fact(4))
print(fact(1))
assert 24 == fact(4), "returns factorial"
assert 1 == fact(1), "factorial of 1 is 1"


