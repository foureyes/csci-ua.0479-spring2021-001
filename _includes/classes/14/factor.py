def largest_factor(num):
	
	current_largest = 1

	# assume we're getting an int

	# don't go up to number, stop just before
	for factor in range(1, num):
		if num % factor == 0:
			current_largest = factor 
	
	return current_largest
print(largest_factor(873))
