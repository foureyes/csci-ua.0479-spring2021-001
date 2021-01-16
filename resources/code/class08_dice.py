"""
>>> d = {}
>>> d = {"first":"joe", "fav_candy": "cleo"}
>>> d
{'first': 'joe', 'fav_candy': 'cleo'}
>>> d2 = {100:[1, 2, 3], "another string": {}}
>>> d2
{'another string': {}, 100: [1, 2, 3]}
>>> d
{'first': 'joe', 'fav_candy': 'cleo'}
>>> d['first']
'joe'
>>> d['fav_candy']
'cleo'
>>> d['last']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'last'
>>> d['first']
'joe'
>>> d.get('first')
'joe'
>>> d['first']
'joe'
>>> d.get('last')
>>> result = d.get('last')
>>> print(result)
None
>>> result = d.get('first')
>>> print(result)
joe
>>> result = d.get('last', 'default value is returned')
>>> print(result)
default value is returned
>>> d
{'first': 'joe', 'fav_candy': 'cleo'}
>>> d
{'first': 'joe', 'fav_candy': 'cleo'}
>>> d['last']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'last'
>>> d['last'] = 'versoza'
>>> d
{'first': 'joe', 'last': 'versoza', 'fav_candy': 'cleo'}
>>> d['middle
  File "<stdin>", line 1
    d['middle
            ^
SyntaxError: EOL while scanning string literal
>>> d['middle']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'middle'
>>> d.get('middle')
>>> d.get('middle', 'quincy')
'quincy'
>>> d
{'first': 'joe', 'last': 'versoza', 'fav_candy': 'cleo'}
>>> d['last'] = 'versoza'
>>> for mystery in d:
...   print(mystery)
...
first
last
fav_candy
>>> for k in d:
...   print(d[k])
...
joe
versoza
cleo
>>> d.items()
dict_items([('first', 'joe'), ('last', 'versoza'), ('fav_candy', 'cleo')])
>>> for k, v in d.items():
...   print(k, v)
...
first joe
last versoza
fav_candy cleo
>>> d.keys()
dict_keys(['first', 'last', 'fav_candy'])
>>> d.values()
dict_values(['joe', 'versoza', 'cleo'])
>>> d
{'first': 'joe', 'last': 'versoza', 'fav_candy': 'cleo'}
>>> d['last'] = 'v'
>>> d
{'first': 'joe', 'last': 'v', 'fav_candy': 'cleo'}
>>> d['last'] = ('v', 'versoza', 'quincy')
>>> d['last']
('v', 'versoza', 'quincy')
>>> d.items()
dict_items([('first', 'joe'), ('last', ('v', 'versoza', 'quincy')), ('fav_candy', 'cleo')])
>>> len(d)
3
>>> 'middle' in d
False
>>> 'fav_candy' in d
True
>>> d
{'first': 'joe', 'last': ('v', 'versoza', 'quincy'), 'fav_candy': 'cleo'}
>>> d.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pop expected at least 1 arguments, got 0
>>> d.pop('fav_candy)
  File "<stdin>", line 1
    d.pop('fav_candy)
                    ^
SyntaxError: EOL while scanning string literal
>>> d.pop('fav_candy')
'cleo'
>>> d
{'first': 'joe', 'last': ('v', 'versoza', 'quincy')}
>>> d = {'first': 'joe', 'last': ('v', 'versoza', 'quincy'), 'fav_candy': 'cleo'}
>>> d
{'first': 'joe', 'last': ('v', 'versoza', 'quincy'), 'fav_candy': 'cleo'}
>>> d.popitem()
('first', 'joe')
>>> d
{'last': ('v', 'versoza', 'quincy'), 'fav_candy': 'cleo'}
>>> d
{'last': ('v', 'versoza', 'quincy'), 'fav_candy': 'cleo'}
>>> d.update({'last':'veeeee'})
>>> d
{'last': 'veeeee', 'fav_candy': 'cleo'}
>>> d.update({'last':'versoze', 'fav_candy':'twizzlers'})
>>> d
{'last': 'versoze', 'fav_candy': 'twizzlers'}
>>> d.update({'last':'versoza', 'first':'joe'})
>>> d
{'first': 'joe', 'last': 'versoza', 'fav_candy': 'twizzlers'}
>>>
"""
import random

counts = {}
{2: 100, 3: 145}
for i in range(1000):
    d1, d2 = random.randint(1, 3), random.randint(1, 3)
    result = d1 + d2
    # create a new key, that is the result of the roll
    # set its value to 1, because its the first time we've
    # seen this roll
    #XXXXXXX counts.update({result: counts[result] + 1})
    # counts[result] could yield a key error so we still have
    # to check
    
    """
    if result in counts:
    	counts[result] = counts[result] + 1
    else:
    	counts[result] = 1
    """
    # if it exists
    # then get will return a value, add one, and we're overwriting countes[result]
    """
    counts[result] = counts.get(result, 0) + 1
    """
    try:
        counts[result] = counts[result] + 1
    except KeyError:
    	counts[result] = 1

    # if it doesn't exist
    # \/ make a new key value pair
    # |                     \/ if it doesn't exist, then set it to 0 
    #counts[result] = counts.get(result, 0) + 1

#for roll, count in counts: XXXX

for roll, count in counts.items():
    print(roll, count)







