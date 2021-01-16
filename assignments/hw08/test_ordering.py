# You'll have to do a bit of sorting (that is, putting values in a 
# specific order) for this assignment. However, dictionaries are not
# ordered! You also aren't allowed to used OrderedDict (which is a
# type that does allow for ordered key/value paris).

# With that said, there are a couple of things that may be helpful!
# 1. the sorted function
# 2. the reverse method (on lists)

# The sorted function takes an iterable object creates a new list 
# with the elements of the iterable object passed in ordered from 
# least to greatest (ascending order). This differs from a list's
# sort method because:
# 1. it returns a new list (the list passed in does not change)
# 2. it allow for options such as reversing the order and chaning
#    the value that will be used to determine order

# Here's an example of the most simple case:
nums = [2, 4, 1, 3]
sorted_nums = sorted(nums)
print('using sorted on a list of numbers...', nums, '\n=====\n')

print('resulting new list is sorted:')
print('sorted_nums:', sorted_nums, '\n') # [1, 2, 3, 4] 

print('original list stays the same:')
print('nums:', nums) # [2, 4, 1, 3] 

# A keyword argument, reverse, can also be passed in to determine
# whether or not the list should be sorted in ascending or 
# descending order. Syntax is: sorted(thing_to_sort, reverse=True)
reverse_sorted_nums = sorted(nums, reverse=True)
print('resulting new list is sorted in descending order:')
print('sorted_nums:', sorted_nums, '\n') # [4, 3, 2, 1]

# How does sorted handle dictionaries? It'll work with the keys.
# Sorting a dictionary on its own will give back a list of keys
# sorted in order of each key.
letter_freq = {'a': 80, 'b': 20, 'c': 40, 'd':30, 'e': 100}
print('Using sorted on a dictionary...', letter_freq, '\n=====\n')

# This will give back a list of keys sorted by key
sorted_freq_1 = sorted(letter_freq)
print('...returns a new sorted list of keys:', sorted_freq_1)

# However, you can also sort a dictionary's keys based on its 
# associated value. This involves passing in another keyword 
# argument called key. The syntax is: key=dictionary_name.get

# Gives back a list of keys sorted by value associated with key
sorted_freq_2 = sorted(letter_freq, key=letter_freq.get)
print('...with key=letter_freq.get, sorts keys by their associated value:', sorted_freq_2, '\n')

# You can also sort a list of tuples with sorted! It'll just
# return a new list sorted based on the first differing element
# of each tuple:
list_of_tuples = [('b', 100), ('c', 50), ('a', 20)]
print('Using sorted on a list of tuples...\n=====\n')

sorted_list_of_tuples = sorted(list_of_tuples)
print('tuples are sorted by first differing element', sorted_list_of_tuples, '\n')

# Finally, a quick way of reversing the order of elements in a list is
# to use the .reverse() method. It is called on an existing list. It 
# will reverse the list in place (it won't return a value; instead, it
# will reverse the list that it was called on.
print('Using reverse\n=====\n')
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers) # [4, 3, 2, 1]
