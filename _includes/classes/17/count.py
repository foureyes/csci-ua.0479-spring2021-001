def count_letters(letter, word):
	"""returns the number of times a letter occurs in a word"""
	count = 0
	for c in word:
		if c == letter:
			count += 1
	return count
assert 3 == count_letters("a", "aardvark"), "should count letters in word"
assert 0 == count_letters("x", "aardvark"), "zero if no letters in word"
