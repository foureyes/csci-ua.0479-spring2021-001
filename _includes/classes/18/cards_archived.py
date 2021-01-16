import random
deck = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A'] * 4
random.shuffle(deck)
player_hand = []
computer_hand = []
for i in range(2):
	player_hand.append(deck.pop())
	computer_hand.append(deck.pop())

def my_sum(li):
	total = 0
	for n in li:
		total += n
	return total

def current_total_v2(hand):
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

def current_total_v1(hand):
	total = 0
	aces = []

	for card in hand:
		if card.isdigit():
			total += int(card)
		elif card in 'JQK':
			total += 10
		elif card == 'A':
			aces.append(1)

	for i in range(len(aces)):
		if total + my_sum(aces) <= 21 - 10:
			aces[i] = 11

	total += my_sum(aces)
	
	return(total)

print(current_total_v2(['A', '9', 'A']))
print(current_total_v2(['A', 'A', '10']))
print(current_total_v2(['A', 'A', 'A', '9']))
print(current_total_v2(['A', '2', 'A', '7']))
			
		
		
"""			
print(player_hand)
print(computer_hand)
"""
print("Your hand is equal to: ")
print(player_hand)
print(current_total_v2(player_hand))
command = input('what do you want to do?')
while command != 's':
	if command == 'h':
		player_hand.append(deck.pop())
	t = current_total_v2(player_hand)
	print(player_hand)
	print(t)
	if t == 21:
		print("you have 21")
		break
	elif t > 21:
		print("you bust")
		break
	command = input('what do you want to do?')

while current_total_v2(computer_hand) < 18:
	computer_hand.append(deck.pop())
print(computer_hand)


