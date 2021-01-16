def caesar_decrypt(s):
	"""decrypts a string that was encrypted by rotating each letter 23 places
	 to the right"""
	encrypted  = 'XYZABCDEFGHIJKLMNOPQRSTUVWxyzabcdefghijklmnopqrstuvw'
	translated = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	decrypted = ''
	for c in s:
		letter_index = encrypted.find(c)
		if letter_index > -1:
			decrypted += translated[letter_index]
		else:
			decrypted += c
	return decrypted

print(caesar_decrypt('Ebiil tloia! www'))
print(caesar_decrypt('xyz uvw'))
expected = 'The quick brown fox jumps over the lazy dog.' 
observed = caesar_decrypt('Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.')
assert expected == observed, 'test decryption'


