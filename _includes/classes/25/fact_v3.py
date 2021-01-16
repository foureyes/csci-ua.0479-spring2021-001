def fact(n):
	if n == 1:
		return 1
	else:
		return n * f(n -1)

print(fact(4))
print(fact(1))
assert 24 == fact(4), "returns factorial"
assert 1 == fact(1), "factorial of 1 is 1"

