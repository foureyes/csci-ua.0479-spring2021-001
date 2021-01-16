word = input("Enter a word\n>")
d = {}
for c in word:
	try:
		d[c] += 1
	except KeyError:
		d[c] = 1
for k,v in d.items():
	print(k, v)
