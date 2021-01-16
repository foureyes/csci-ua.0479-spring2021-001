board = []
for number in range(8, 0, -1):
	row = []
	for letter in "abcdefgh":
		row.append("%s%s" % (letter,number))
	board.append(row)
print(board)
