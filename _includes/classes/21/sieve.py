def all_primes_below(upper_bound):

	primes = []
	non_primes = []

	# starting with 2, populate list of non_primes by counting by p
	for p in range(2, upper_bound):
		
		# don't both populating non_primes with non_prime multiples 
		if p not in non_primes:
			primes.append(p)
			
			# drop all multiples into non_prime list
			for multiple in range(p + p, upper_bound, p):
				non_primes.append(multiple)
	return primes
print(all_primes_below(121))
