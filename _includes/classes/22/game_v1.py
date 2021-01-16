import random

def outcome(hand_one, hand_two):
	if hand_one == hand_two:
		return None
	if hand_one == 'r' and hand_two == 's' or hand_one == 'p' and hand_two =='r' or hand_one == 's' and hand_two == 'p':
		return 1
	else:
		return 2

assert 1 == outcome('p', 'r')
assert 1 == outcome('s', 'p')
assert 1 == outcome('r', 's')
assert 2 == outcome('r', 'p')
assert 2 == outcome('p', 's')
assert 2 == outcome('s', 'r')
assert None == outcome('r', 'r')
assert None == outcome('s', 's')
assert None == outcome('s', 's')
		
hands = ['r', 'p', 's']

command = ''
player_score = 0
computer_score = 0
while command != 'q':
	command = input("(r)ock, (p)aper, (s)cissors or (q)uit\n>")
	if command == 'q':
		break
	elif command in hands:
		computer_move = random.choice(hands)
		winner = outcome(command, computer_move)
		print("PLAY: player: %s, computer: %s" % (command, computer_move)) 
		if winner == 1:
			print("player wins")
			player_score += 1
		elif winner == 2:
			print("computer wins")
			computer_score += 1
		else:
			print("tie")
			# tie
		print("SCORE: player: %s, computer: %s" % (player_score, computer_score)) 
	else:
		print("I don't know that command")	
