def human_readable_list(v):
	length = len(v)
	if length == 0:
		return ""
	elif length == 1:
		return str(v[0])
	elif length == 2:
		return " and ".join(v)
	else:
		last = v.pop()
		return "%s, and %s" % (", ".join(v), last)

assert "foo, bar, and baz" == human_readable_list(["foo", "bar", "baz"]), "3 or more elements are comma separated with serial comma before and"
assert "foo and bar" == human_readable_list(["foo", "bar"]), "2 elements are separated by and"
assert "foo" == human_readable_list(["foo"]), "1 element gives back element"
assert "" == human_readable_list([]), "empty list gives back empty string"

