def fact(n):
	for i in range(n - 1, 0, -1):
		n = n * i
	return n

print(fact(4))
print(fact(1))
assert 24 == fact(4), "returns factorial"
assert 1 == fact(1), "factorial of 1 is 1"



