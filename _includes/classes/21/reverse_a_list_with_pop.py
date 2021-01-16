def rev(a):
	new_list = []
	while(len(a) != 0):
		new_list.append(a.pop())
	return new_list

my_stuff = ["will", "soon", "disappear"]
print(my_stuff)
print(rev(my_stuff))
print(my_stuff)
