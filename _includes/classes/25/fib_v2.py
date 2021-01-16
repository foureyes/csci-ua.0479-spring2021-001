def fib(n):
	total = 0
	if n == 0 or n == 1:
		return n
	else:
		res =  fib(n - 1) + fib(n - 2)
		return res
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(9))

