word = input("Enter a word to translate or type 'quit' to leave the program\n> ")
while word != 'quit':
	if word == 'cat':
		print('gato')
	elif word == 'dog':
		print('perro')
	else:
		print('no se')
	word = input("Enter a word to translate or type 'quit' to leave the program\n> ")
print('Adios!')
