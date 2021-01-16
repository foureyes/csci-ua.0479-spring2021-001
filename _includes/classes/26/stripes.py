def draw_an_x(n):
	""" returns an x """
	# create an empty string to hold the X
	pattern = ""

	# start the first for loop, these will represent rows
	for i in range(n):
		# each row is going to start off as an empty string
		line = ""

		# the second loop will represent every item in a row 
		for j in range(n):
			# only draw the diagonals based on these conditions
			if i + j == n - 1 or i == j:
				line += "O"
			else:
				line += " "	
		pattern += line + "\n"
	return pattern
print(draw_an_x(10))

