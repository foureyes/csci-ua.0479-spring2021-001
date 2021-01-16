def all_primes_below(upper_bound):
	prime_numbers = [True] * upper_bound 
	p = 2
	while p * p < upper_bound:
		for i in range(p, upper_bound, p):
			if i != p:
				prime_numbers[i] = False
		p += 1
		while prime_numbers[p] == False:
			p += 1
	new_list = []
	for i in range(upper_bound):
		if prime_numbers[i]:
			new_list.append(i)
	return new_list
		 
print(all_primes_below(121))

