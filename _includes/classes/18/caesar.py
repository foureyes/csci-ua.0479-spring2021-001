def shift_letters(shift, s):
	uppercase_start, lowercase_start = 65, 97
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	translation = ''
	for c in s:
		letter_pos = alphabet.find(c.upper())
		offset = (letter_pos + shift) % len(alphabet)
		if c.isupper():
			translation += chr(uppercase_start + offset)
		elif c.islower():
			translation += chr(lowercase_start + offset)
		else:
			translation += c
	return translation

print('Caesar Cipher\n==========\n')
action = ''

while action != 'q':
	action = input('(e)ncrypt, (d)ecrypt or (q)uit)?\n> ')
	if action == 'q':
		print('Bye!')
	elif action == 'e':
		shift = int(input('How many places should each letter be shifted?\n> '))
		message = input('What is the message?\n> ')
		print(shift_letters(shift, message))
	elif action == 'd':
		shift = int(input('How many places was each letter shifted?\n> '))
		message = input('What was the message?\n> ')
		print(shift_letters(-shift, message))
	else:
		print('Sorry, I can only encrypt, decrypt or quit...')
