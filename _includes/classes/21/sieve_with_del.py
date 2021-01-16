def all_primes_below(upper_bound):
	prime_numbers = list(range(2, upper_bound))
	min_index = 0
	p = prime_numbers[min_index]
	while p * p < upper_bound:
		i = min_index
		while(i < len(prime_numbers) - 1):
			if prime_numbers[i] % p == 0 and prime_numbers[i] != p:
				del prime_numbers[i]
			i += 1
		min_index += 1
		p = prime_numbers[min_index]
		print("%s - %s"  % (p, prime_numbers))
		 
print(all_primes_below(121))

