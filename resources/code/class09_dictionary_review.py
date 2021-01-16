"""
>>> empty = {}
>>> person = {'first': 'joe', 'num_pets': 2}
>>> generic_d = {(1, 2): 'what???'}
>>> person['first']
'joe'
>>> person['num_pets']
2
>>> person['num_pets']
2
>>> person['fav_food']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'fav_food'
>>> result = person.get('fav_food')
>>> print(result)
None
>>> result = person.get('fav_food', 'shaved ice w red beans')
>>> print(result)
shaved ice w red beans
>>> person
{'num_pets': 2, 'first': 'joe'}
>>> person['fav_food
  File "<stdin>", line 1
    person['fav_food
                   ^
SyntaxError: EOL while scanning string literal
>>> person['fav_food']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'fav_food'
>>> person['fav_food'] = 'empanadas'
>>> person
{'fav_food': 'empanadas', 'num_pets': 2, 'first': 'joe'}
>>> empty
{}
>>> len(person)
3
>>> 'height' in person
False
>>> 'first' in person
True
>>> 'first' not in person
False
>>> for mystery in person:
...   print(mystery)
...
fav_food
num_pets
first
>>> for k in person:
...   print(person[k])
...
empanadas
2
joe
>>> for k in person:
...   print(k, person[k])
...
fav_food empanadas
num_pets 2
first joe
>>> points = [(1, 2), (30, 40), (99, 100)]
>>> for p in points:
...   print(p)
...
(1, 2)
(30, 40)
(99, 100)
>>> t = 'hello', 'bye'
>>> a, b = t
>>> a
'hello'
>>> b
'bye'
>>> points
[(1, 2), (30, 40), (99, 100)]
>>> for x, y in points:
...   print(x, y)
...
1 2
30 40
99 100
>>> points.append((1, 2, 3))
>>> for x, y in points:
...   print(x, y)
...
1 2
30 40
99 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
>>> person
{'fav_food': 'empanadas', 'num_pets': 2, 'first': 'joe'}
>>> list(person.items())
[('fav_food', 'empanadas'), ('num_pets', 2), ('first', 'joe')]
>>> for k, v in person.items():
...   print(k, v)
...
fav_food empanadas
num_pets 2
first joe
>>> person
{'fav_food': 'empanadas', 'num_pets': 2, 'first': 'joe'}
>>> person.update({'first': 'joseph', 'height':'around 5???'})
>>> person
{'fav_food': 'empanadas', 'height': 'around 5???', 'num_pets': 2, 'first': 'joseph'}
>>> person.popitem()
('fav_food', 'empanadas')
>>> person
{'height': 'around 5???', 'num_pets': 2, 'first': 'joseph'}
>>> person.pop('height')
'around 5???'
>>> person
{'num_pets': 2, 'first': 'joseph'}
>>> nums = [5, 1, 4, 2, 3]
>>> nums.sort()
>>> nums
[1, 2, 3, 4, 5]
>>> nums = [5, 1, 4, 2, 3]
>>> copy = nums[:]
>>>
>>> copy.sort()
>>> copy
[1, 2, 3, 4, 5]
>>> nums
[5, 1, 4, 2, 3]
>>> sorted
<built-in function sorted>
>>> sorted(nums)
[1, 2, 3, 4, 5]
>>> nums
[5, 1, 4, 2, 3]
>>> points
[(1, 2), (30, 40), (99, 100), (1, 2, 3)]
>>> import random
>>> random.shuffle(points)
>>> points
[(99, 100), (30, 40), (1, 2), (1, 2, 3)]
>>> sorted(points)
[(1, 2), (1, 2, 3), (30, 40), (99, 100)]
>>> person
{'num_pets': 2, 'first': 'joseph'}
>>> person['last'] = 'versoza'
>>> person
{'last': 'versoza', 'num_pets': 2, 'first': 'joseph'}
>>> sorted(person)
['first', 'last', 'num_pets']
>>> num
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'num' is not defined
>>> nums
[5, 1, 4, 2, 3]
>>> sorted(nums, reverse=true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> sorted(nums, reverse=True)
[5, 4, 3, 2, 1]
>>> sorted(points, reverse=True)
[(99, 100), (30, 40), (1, 2, 3), (1, 2)]
>>> person
{'last': 'versoza', 'num_pets': 2, 'first': 'joseph'}
>>> d = {'a': 100, 'b': 200, 'c':150}
>>> sorted(d, key=d.get)
['a', 'c', 'b']
>>> sorted_keys = sorted(d, key=d.get)
>>> for k in sorted_keys:
...   print(k, d[k])
...
a 100
c 150
b 200
>>>
"""
