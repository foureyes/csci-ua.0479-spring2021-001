word = input("Enter a word\n>")
d = {}
for c in word:
	d[c] = d.get(c, 0) + 1
for k,v in d.items():
	print(k, v)
