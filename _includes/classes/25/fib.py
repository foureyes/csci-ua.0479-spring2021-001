def fib(n):
	i = 0
	cur = 1
	prev = 1
	prev_prev = 0
	while i < n:
		print(cur)
		prev_prev = prev
		prev = cur 
		cur = prev + prev_prev
		i += 1
		
		
fib(8)
