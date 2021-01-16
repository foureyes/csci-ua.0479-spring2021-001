def last_to_first(items):
	""" makes last element in list first, shifts every other element up one """
	if len(items) <= 1:
		return items
	else: 
		return [items[-1]] + items[0:-1]

assert [1] == last_to_first([1]), 'test that one element returns same list'
assert [] == last_to_first([]), 'test that empty list returns empty list'
assert [4, 1, 2, 3] == last_to_first([1, 2, 3, 4]), 'test that all elements shifted by one'
