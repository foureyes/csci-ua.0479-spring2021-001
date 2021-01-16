def caesar_decrypt(s):
	"""decrypts a string that was encrypted by rotating each letter 23 places
	 to the right"""
	uppercase_start, lowercase_start = 65, 97
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	shift = 23
	translation = ''
	for c in s:
		letter_pos = alphabet.find(c.upper())
		offset = (letter_pos - shift) % 26 
		if c.isupper():
			translation += chr(uppercase_start + offset)
		elif c.islower():
			translation += chr(lowercase_start + offset)
		else:
			translation += c
	return translation

print(caesar_decrypt('Ebiil tloia! www'))
print(caesar_decrypt('xyz uvw'))
expected = 'The quick brown fox jumps over the lazy dog.' 
observed = caesar_decrypt('Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.')
assert expected == observed, 'test decryption'


