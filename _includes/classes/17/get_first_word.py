def get_first_word(sentence):
	"""returns the first word in a sentence"""
	index = 0
	for c in sentence:
		if c == " ":
			break
		index += 1
	return sentence[0:index]

assert "hi" == get_first_word("hi there!"), "returns first word"
assert "hi" == get_first_word("hi"), "returns word if only one word"
assert "" == get_first_word("  "), "returns empty if only white space"
assert "" == get_first_word(""), "returns empty if sentence is empty"
# print(get_first_word("hi there!"))
# print(get_first_word("hi"))
