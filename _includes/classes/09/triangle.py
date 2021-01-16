# create an empty  string to hold the triangle
triangle = ''
for row in range(1, 6):

	# create a string to hold the current row
	row_of_stars = ''

	# keep on adding stars based on the current row
	for col in range(row):
		row_of_stars += '*'

	# add the row to the triangle with a new line
	triangle += row_of_stars + '\n'

print(triangle)

