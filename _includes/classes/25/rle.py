def encode(s):
	cur_letter = None
	cur_letter_count = 0
	letter_list = []
	for letter in s:
		# print(letter, cur_letter, cur_letter_count)
		# if there's a change in letter... count it
		if letter != cur_letter:
			# guard against the initial case 
			if cur_letter is not None:
				letter_list.append((cur_letter, cur_letter_count))
			# otherwise, we'll always reset
			cur_letter = letter
			cur_letter_count = 1
		else:
			cur_letter_count += 1
	letter_list.append((cur_letter, cur_letter_count))
	encoded = ""
	for letter, count in letter_list:
		encoded = encoded + str(count) + letter
	return encoded

word = "tutt"
# print("%s encoded is %s" % (word, encode(word)))
assert "1t1u2t" == encode(word)

word = "whaaaaat the what???"
# print("%s encoded is %s" % (word, encode(word)))
assert "1w1h5a1t1 1t1h1e1 1w1h1a1t3?" == encode(word)

