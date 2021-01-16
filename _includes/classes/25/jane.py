f = open("pg1342.txt", "r")
d = {}
while True:
	line = f.readline()
	if len(line) == 0:
		break
	words = line.split(" ")
	for word in words:
		w = word.strip()
		if len(w) > 0 and w[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			d[w] = d.get(w, 0) + 1
	
for w in sorted(d, key=d.get, reverse=True):
	print(w, d[w])

