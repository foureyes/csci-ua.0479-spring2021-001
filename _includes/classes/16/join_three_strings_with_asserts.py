def join_three_strings(a, b, c):
	return "%s%s%s" % (a, b, c)

assert "ha ha ha" == join_three_strings("ha", "ha", "ha"), "should have spaces"
