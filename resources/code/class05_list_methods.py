"""
methods that change original list
and return nothing (None)
"""

"""
add a new element to a list
* append
* extend 
* insert

removing
* remove
* pop
(del is a statement, but it does remove an element)

misc
* sort
"""
"""
>>> cats
['chairman meow', 'paw newman', 'kitty purry']
>>> cats.append(['bill furry', 'india'])
>>> len(cats)
4
>>> cats.extend(['garfield', 'tom', 'felix'])
>>> cats
['chairman meow', 'paw newman', 'kitty purry', ['bill furry', 'india'], 'garfield', 'tom', 'felix']
>>> cats.extend('abc')
>>> cats
['chairman meow', 'paw newman', 'kitty purry', ['bill furry', 'india'], 'garfield', 'tom', 'felix', 'a', 'b', 'c']
>>> cats = cats[0:3]
>>> cats
['chairman meow', 'paw newman', 'kitty purry']
>>> cats.insert(1, 'heathcliff')
>>> cats
['chairman meow', 'heathcliff', 'paw newman', 'kitty purry']
>>>
>>> cats
['chairman meow', 'heathcliff', 'paw newman', 'kitty purry']
>>> cats[1:3]
['heathcliff', 'paw newman']
>>> cats
['chairman meow', 'heathcliff', 'paw newman', 'kitty purry']
>>> cats = cats[1:3]
"""

"""
using a for loop
it goes over every element in a collection of elements (iterable object)

what determines number of iterations?
the number of elements in your iterable object

sooo....if your object shrinks, then the number iterations also changes
"""
"""
words = ['foo', 'foo', 'foo', 'bar', 'baz']

print(words)


while 'foo' in words:
    words.remove('foo')

print(words)

"""
"""
>>> cats
['chairman meow', 'paw newman', 'kitty purry', 'heathcliff', 'wordsworth']
>>> cats
['chairman meow', 'paw newman', 'kitty purry', 'heathcliff', 'wordsworth']
>>> result = cats.pop()
>>> cats
['chairman meow', 'paw newman', 'kitty purry', 'heathcliff']
>>> print(result)
wordsworth
>>> print(result)
wordsworth
>>> cats
['chairman meow', 'paw newman', 'kitty purry', 'heathcliff']
>>> cats.pop(1)
'paw newman'
>>> cats
['chairman meow', 'kitty purry', 'heathcliff']
>>> cats
['chairman meow', 'kitty purry', 'heathcliff']
>>> cats.sort()
>>> cats
['chairman meow', 'heathcliff', 'kitty purry']
>>> cats
['chairman meow', 'heathcliff', 'kitty purry']
>>> cats.index('kitty purry')
2
>>> cats.index('does not exist')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'does not exist' is not in list
>>> cats.count('chairman meow')
1
>>> cats
['chairman meow', 'heathcliff', 'kitty purry']
>>> animals[cats, ['bark twain', 'jane pawsten']]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'animals' is not defined
>>> animals = [cats, ['bark twain', 'jane pawsten']]
>>> animals
[['chairman meow', 'heathcliff', 'kitty purry'], ['bark twain', 'jane pawsten']]
>>> for animal_list in animals:
...   print(type(animal_list))
...
<class 'list'>
<class 'list'>
>>> for lst in animals:
...   for ele in lst:
...     print(ele)
...
chairman meow
heathcliff
kitty purry
bark twain
jane pawsten
>>> animals
[['chairman meow', 'heathcliff', 'kitty purry'], ['bark twain', 'jane pawsten']]
>>> animals[0]
['chairman meow', 'heathcliff', 'kitty purry']
>>> animals[0][-1]
'kitty purry'
>>>
"""

"""
double_every_element(numbers)
parameters:
numbers: list of numbers
return: a entirely new list composed of every number in the original doubled
body: ^^^^^
"""
# write this function, come up with some tests

# map - transform every element in a list and produce a new list
def double_every_element(numbers):
	"""accumulator that will hold all doubled elements and will be returned
	"""
	new_list = []	
	"""... go over every element in the numbers list
	"""
	for num in numbers:
		"""num will represent the element that we're looking at"""
		"""add the doubled version to new_list"""
		doubled = num * 2
		"""changing the accumulator"""
		new_list.append(doubled)
	return new_list
# when you design a function... it should only do one thing
		
"""
print(double_every_element([1, 2, 3]))
result = double_every_element([100, 200, 300])
print(result)
"""
"""
get_even_numbers(numbers)
parameter: numbers list
return: a new list that is composed of only even numbers
body: ^^^ that calculation
"""
"""
def is_even(n):
	return n % 2 == 0

def get_even_numbers(numbers):
	filtered_list = []
	for num in numbers:
		if is_even(num):
			filtered_list.append(num)
	return filtered_list

nums = [2, 3, 4, 5, 6]
print(get_even_numbers(nums))
"""



		



































































