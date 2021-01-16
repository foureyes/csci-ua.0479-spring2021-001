import random
ones = 0
for count in range(1, 1000):
	roll = random.randint(1, 6)
	if roll == 1:
		ones = ones + 1
print(str(ones) + " of 1000 rolls were ones")
