import random
ones = 0
count = 0
while count < 1000:
	roll = random.randint(1, 6)
	if roll == 1:
		ones = ones + 1
	count = count + 1
print(str(ones) + " of 1000 rolls were ones")
