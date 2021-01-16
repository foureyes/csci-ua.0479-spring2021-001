def current_total(hand):
	""" Sums the cards in hand.  Aces count as 1 or 11.  Will optimize for 
	highest total without going over 21. """
	total, aces = 0, 0
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
	return total

assert 21 == current_total(['A', '9', 'A']), "two aces, one 11 and one 1"
assert 12 == current_total(['A', 'A', '10']), "two aces, both 1"
assert 21 == current_total(['A', 'A', 'A', '8']), "three aces, one 11 and two 1"
assert 12 == current_total(['A', 'A', 'A', '9']), "three aces, three 1"
