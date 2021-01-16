def rev(a):
	new_list = []
	for i in range(len(a) - 1, -1, -1):
		new_list.append(a[i])	
	return new_list
		
assert ["charlie", "bravo", "alpha"] == rev(["alpha", "bravo", "charlie"]), "reverses order of non-empty list"
assert [] == rev([]), "returns empty list for empty list"
print(rev(["alpha", "bravo", "charlie"]))
