def caesar_encrypt(s):
	"""encrypts a string by rotating each letter 23 places to the right"""
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	shifted  = 'XYZABCDEFGHIJKLMNOPQRSTUVWxyzabcdefghijklmnopqrstuvw'
	translation = ''
	for c in s:
		letter_index = alphabet.find(c)
		if letter_index > -1:
			translation += shifted[letter_index]
		else:
			translation += c
	return translation

print(caesar_encrypt('Hello world! zzz'))
print(caesar_encrypt('abc xyz'))
expected = 'Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.'
observed = caesar_encrypt('The quick brown fox jumps over the lazy dog.')
assert expected == observed, 'test encryption'

