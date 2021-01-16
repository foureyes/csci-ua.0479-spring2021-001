def is_digit(s):
	"""determines if a string is numeric (only contains 0 through 9)"""
	if s == "":
		return False

	for c in s:
		if c not in "0123456789":
			return False

	return True

assert True == is_digit("58723"), "true of all characters are numeric "
assert False == is_digit("twelve"), "false if not all characters are numeric"
assert False == is_digit("12 ducks"), "false if not all characters are numeric"
assert False == is_digit(""), "false if empty string"
# print(is_digit("43"))
