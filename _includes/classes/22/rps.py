import random
def get_next_move(their_moves, your_moves):
	possible_moves = ['r', 'p', 's']
	if their_moves != []:
		last_move = their_moves[-1]
		if last_move == 'r':
			next_move = 'p'
		elif last_move == 'p':
			next_move = 's'
		elif last_move == 's':
			next_move = 'r'
	else:
		next_move = random.choice(possible_moves)
	return next_move
