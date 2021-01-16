import random

number_of_attempts = 10
total_rolls = 0

for attempt in range(number_of_attempts):
	number_of_rolls, roll1, roll2 = 0, 0, 0
	while roll1 + roll2 != 7:
		roll1 = random.randint(1, 6)
		roll2 = random.randint(1, 6)
		number_of_rolls += 1
		print(str(roll1) + "," + str(roll2) + ": " + str(roll1 + roll2))
	print("-----\n" + str(number_of_rolls) + " rolls\n")
	total_rolls += number_of_rolls
print("Average: " + str(total_rolls / number_of_attempts) + " rolls")
	
