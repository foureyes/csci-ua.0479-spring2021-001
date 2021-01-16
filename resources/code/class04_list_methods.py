"""
List Methods
=====

Background
-----

An object is a _thing_ that a variable can refer to

* it can hold some data ... for example, a range objects holds the numbers in the sequence
* it can also perform some actions

Actions / Methods
-----
* an action is also called a method
* a method is a function in the context of an object
* use the dot operator to call a method on an object

Example:

s = 'hello'
print(s.upper()) <--- returns 'HELLO'

Every value in python is an object
"""

"""
Lists Methods!
=====

Adding stuff to a list
-----
Note that none of these methods return a value! (That is, you get back None if you assign result
to a variable)
1. append(element): takes one argument and adds it to the end of the list
2. extend(sequence): takes one argument (that's a sequence) and adds each individual element as a 
   separate element in list that extend is called on
3. insert(i, element): inserts argument before index, i

Example of no return value:
dogs = ['terrier']
result = dogs.append('poodle')
print(result) # None
print(dogs) # ['terrier', 'poodle']

getting rid of stuff
-----
1. remove(element): removes first occurence of value, element, in list called on
2. pop: removes last element AND returns it <-- one of the few list elements that actually returns a value
Note that there's also an operator:
del <-- not a method, just an operator
del some_list[1] # removes 2nd element

misc
-----
sort <-- sort in ascending order in place does not return anythying
index <-- give back the index of an element in a list... or error if it doesn't exist returns index
count <-- counts the number of occ of element in list returns count
"""

"""
>>> words = ['foo', 'bar', 'baz', 'qux', 'corge']
['foo', 'bar', 'baz', 'qux', 'corge']
>>> dir(words)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dogs = []
>>> dogs.append('terrier')
>>> dogs
['terrier']
>>> dogs.append('pug')
>>> dogs
['terrier', 'pug']
>>> dogs.append(['doge', 'corgie'])
>>> dogs
['terrier', 'pug', ['doge', 'corgie']]
>>> dogs[2][1]
'corgie'
>>> dogs[-1][-1]
'corgie'
>>> dogs[0] = 'poodle'
>>> dogs
['poodle', 'pug', ['doge', 'corgie']]
>>> dogs[2][0] = 'chug'
>>> dogs
['poodle', 'pug', ['chug', 'corgie']]
>>> dogs[0][0]
'p'
>>> dogs[0][0] = 'd'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> dogs
['poodle', 'pug', ['chug', 'corgie']]
>>> dogs.extend(['terrier','st. bernard'])
>>> dogs
['poodle', 'pug', ['chug', 'corgie'], 'terrier', 'st. bernard']
>>> cats = ['maine coone', 'russian blue']
>>> dogs.extend(cats)
>>> dogs
['poodle', 'pug', ['chug', 'corgie'], 'terrier', 'st. bernard', 'maine coone', 'russian blue']
>>> words
['foo', 'bar', 'baz', 'qux', 'corge']
>>> words.insert(0, 'surprise!')
>>> words
['surprise!', 'foo', 'bar', 'baz', 'qux', 'corge']
>>> result = words.insert(0, 'did not expect that')
>>> print(result)
None
>>> dogs
['poodle', 'pug', ['chug', 'corgie'], 'terrier', 'st. bernard', 'maine coone', 'russian blue']
>>> dogs.remove('maine coone')
>>> dogs
['poodle', 'pug', ['chug', 'corgie'], 'terrier', 'st. bernard', 'russian blue']
>>> del dogs[-1]
>>> dogs
['poodle', 'pug', ['chug', 'corgie'], 'terrier', 'st. bernard']
>>> result = dogs.pop()
>>> dogs
['poodle', 'pug', ['chug', 'corgie'], 'terrier']
>>> print(result)
st. bernard
>>> nums = [5, 1, 2, 9, 1]
>>> nums.sort()
>>> nums
[1, 1, 2, 5, 9]
>>> nums.count(1)
2
>>> nums
[1, 1, 2, 5, 9]
>>> nums.index(9)
4
>>> nums.index('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'hello' is not in list
>>> dogs
['poodle', 'pug', ['chug', 'corgie'], 'terrier']
>>> 'pug' in dogs
True
>>> 'maine coon' in dogs
False
>>> 'maine coon' not in dogs
True
>>> 'chug' in dogs
False
>>> dogs
['poodle', 'pug', ['chug', 'corgie'], 'terrier']
>>> del dogs[2]
>>> dogs
['poodle', 'pug', 'terrier']
>>> new_list = []
>>> for dog in dogs:
...   new_list.append(dog.upper()
...
... )
...
>>> new_list
['POODLE', 'PUG', 'TERRIER']
>>> dogs
['poodle', 'pug', 'terrier']
>>> dogs
['poodle', 'pug', 'terrier']
>>> filtered_dogs = []
>>> for dog in dogs:
...   if dog[0] == 'p':
...     filtered_dogs.append(dog)
...
>>> filtered_dogs
['poodle', 'pug']
"""




















