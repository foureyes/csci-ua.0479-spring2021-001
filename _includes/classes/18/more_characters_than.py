def more_characters_than(words, min):
	new_list = []
	for word in words:
		if len(word) > min:
			new_list.append(word)
	return new_list

assert ['zebra', 'tiger'] == more_characters_than(["zebra", "cow", "tiger"], 4), "only strings with more than 4 characters"
assert [] == more_characters_than([], 4), "an empty list returns an empty list"
