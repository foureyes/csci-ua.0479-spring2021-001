def letter_in_word(letter, word):
	result = False
	for c in word:
		if c == letter:
			result = True
			break
	return result

assert True == letter_in_word('c', "chihuahua"), "letter is in word"
assert False == letter_in_word('x', "chihuahua"), "letter is not in word"
