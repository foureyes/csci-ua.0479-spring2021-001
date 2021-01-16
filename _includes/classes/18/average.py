def average(numbers):
	sum = 0
	for n in numbers:
		sum += n
	return sum / len(numbers)

assert 9 == average([2, 3, 4]), "takes a list of integers and returns the average value"
