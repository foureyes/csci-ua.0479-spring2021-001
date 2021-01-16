def caesar_encrypt(s):
	"""encrypts a string by rotating each letter 23 places to the right"""
	uppercase_start, lowercase_start = 65, 97
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	shift = 23
	translation = ''
	for c in s:
		letter_pos = alphabet.find(c.upper())
		offset = (letter_pos + shift) % 26 
		if c.isupper():
			translation += chr(uppercase_start + offset)
		elif c.islower():
			translation += chr(lowercase_start + offset)
		else:
			translation += c
	return translation

print(caesar_encrypt('Hello world! zzz'))
print(caesar_encrypt('abc xyz'))
expected = 'Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.'
observed = caesar_encrypt('The quick brown fox jumps over the lazy dog.')
assert expected == observed, 'test encryption'

