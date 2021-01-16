
def first_n_primes(n):
	"""returns a list of the first n prime numbers""" 
	list_of_primes = []
	# the current number that we're checking the primality of
	candidate = 2

	# keep on finding primes until our list has enough elements
	while len(list_of_primes) < n:
		# assume that we have a prime number
		is_prime = True

		# use trial division to determine if it's not prime
		for i in range(2, candidate):
			# once we know it's not prime, break!
			if candidate % i == 0:
				is_prime = False
				break
		if is_prime:
			list_of_primes.append(candidate)
		candidate += 1
	return list_of_primes
print(first_n_primes(100))
	
