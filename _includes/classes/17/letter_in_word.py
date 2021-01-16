def letter_in_word(letter, word):
	""" determines whether or not a letter is in a word"""
	for c in word:
		if c == letter:
			return True
	return False

assert True == letter_in_word('x', "ox"), "letter is in word"
assert False == letter_in_word('y', "ox"), "letter is not in word"
