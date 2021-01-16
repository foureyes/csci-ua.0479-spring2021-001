word = input("Enter a word\n>")
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
	count = word.count(c)
	if count > 0:
		print(c, count)
