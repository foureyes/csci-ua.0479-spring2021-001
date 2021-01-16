def rle_v1(word):
	"""strings"""
	s = ''
	cur_letter = None
	cur_letter_count = 0
	for c in word:
		# reset if we've transitioned to a new letter
		if c != cur_letter:
			
			# add our previous letter and count to the string
			if cur_letter is not None:
				s += str(cur_letter_count) + cur_letter
			cur_letter = c
			cur_letter_count = 1
		else:
			# just add more to the count
			cur_letter_count += 1

	# we've reached the end, so there's one more count/letter combo left
	s += str(cur_letter_count) + cur_letter
	return s

print(rle_v1('cccaaabbb'))
print(rle_v1('c'))
print(rle_v1('ccc'))
print(rle_v1(''))
	
