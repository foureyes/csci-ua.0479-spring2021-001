def is_a_david_lynch_movie(s):
	if s == "Blue Velvet" or s == "Dune" or s == "Lost Highway":
		return True
	else:
		return False

movie = input("Give me a movie title\n>")
while movie != 'q':
	if is_a_david_lynch_movie(movie):
		print("%s a David Lynch movie!" % (movie))
	else:
		print("There's a fish in the percolator")
	movie = input("Give me a movie title\n>")
