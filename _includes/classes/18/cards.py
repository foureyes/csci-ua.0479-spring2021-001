import random

def current_total(hand):
	""" Sums the cards in hand.  Aces count as 1 or 11.  Will optimize for 
	highest total without going over 21.
	"""
	total = 0
	aces = 0

	for card in hand:
		if card.isdigit():
			total += int(card)
		elif card in 'JQK':
			total += 10
		elif card == 'A':
			aces += 1
			total += 11

	for i in range(aces):
		if total > 21:
			total -= 10
	
	return(total)

assert 21 == current_total(['A', '9', 'A']), "two aces, one 11 and one 1"
assert 12 == current_total(['A', 'A', '10']), "two aces, both 1"
assert 21 == current_total(['A', 'A', 'A', '8']), "three aces, one 11 and two 1"
assert 12 == current_total(['A', 'A', 'A', '9']), "three aces, three 1"

def main():
	
	# create deck and deal
	deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
	random.shuffle(deck)
	player_hand = []
	computer_hand = []
	for i in range(2):
		player_hand.append(deck.pop())
		computer_hand.append(deck.pop())

	# ask for command
	player_total = current_total(player_hand)
	print("Your hand: %s, total: %s" % (player_hand, player_total))
	command = input('What do you want to do? (h)it or (s)tay?\n>')
	while command.lower() != 's':
		if command.lower() == 'h':
			player_hand.append(deck.pop())
		player_total = current_total(player_hand)
		print("Your hand: %s, total: %s" % (player_hand, player_total))
		if player_total == 21:
			print("You have 21")
			break
		elif player_total > 21:
			print("You bust")
			break
		command = input('What do you want to do? (h)it or (s)tay?\n>')

	# let computer move...
	while current_total(computer_hand) < 20:
		computer_hand.append(deck.pop())
	computer_total = current_total(computer_hand)

	# determine who won
	print("Computer hand: %s, total: %s" % (computer_hand, computer_total))
	if player_total <= 21 and (player_total > computer_total or computer_total > 21):
		print("PLAYER WINS")
	elif player_total == computer_total or player_total > 21 and computer_total > 21:
		print("NO ONE WINS")
	else:
		print("COMPUTER WINS")

main()
