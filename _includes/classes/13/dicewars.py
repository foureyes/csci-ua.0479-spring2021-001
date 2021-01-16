
import random
player_score, computer_score, play_game = 0, 0, True 
while play_game:
	command = input("Enter a command: roll or quit\n>")
	if command == 'roll':
		player_roll = random.randint(1, 6)
		computer_roll = random.randint(1, 6)
		print("Player rolled: " + str(player_roll))
		print("Computer rolled: " + str(computer_roll))
		if player_roll > computer_roll:
			print("Player won!")
			player_score += 1
		elif player_roll < computer_roll:
			print("Computer won!")
			computer_score += 1
		elif player_roll == computer_roll:
			print("Tie!")
	elif command == 'quit':
		play_game = False
		print("Bye! The final score was...")
	else:
		print("I don't know that command")
	print("Player: " + str(player_score) + "         Computer: " + str(computer_score) + "\n")
