"""
strings, tuples, lists (compound data types):
* all sequence types
* ordered collection of values
* add sequences together, loop over them, repeat, index into them, slice, len
"""
"""
dictionary is a mapping type:
* a value to a name (key)
* not ordered
* a grab bag of name and value pairs
* {} # empty dictionary
* {name1:value1, name2:value2}
* names (keys) must be an immutable type
* values can be anything

key is 'course number' (immutable because it's a string)
value is 1120
{'course number': 1120}

you can create your own key value pairs, even during run time (when program is running)
"""
"""
import random

twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
for number_of_roll in range(1000):
    roll1 = random.randint(1, 3)
    roll2 = random.randint(1, 3)
    total = roll1 + roll2
    if total == 2:
        twos += 1
    elif total == 3:
        threes += 1
    elif total == 4:
        fours += 1
    elif total == 5:
        fives += 1
    elif total == 6:
        sixes += 1

print(twos, 'twos')
print(threes, 'threes')
print(fours, 'fours')
print(fives, 'fives')
print(sixes, 'sixes')
print(2, twos // 10 * 'X' )
print(3, threes // 10 * 'X' )
print(4, fours // 10 * 'X' )
print(5, fives // 10 * 'X' )
print(6, sixes // 10 * 'X' )
"""
# read a value from a dictionary based on
# d[key]
person = {'first': 'joe'}
print(person['first'])
print(person)
#print(person['last'])
person['first'] = 'patrick'
print(person['first'])
print(person)


"""
dictionaries are good at aggregating data into a single "value"
so that you're not just using basic strings or ints
"""
# 0 is number
course = [[1120],['saray', 'patrick']]
course = {'number': 1120, 'students': ['sarah', 'patrick'], 'name': 'intro to programming'}
print(course)
print(course['students'])
print(','.join(course['students']))
print(course['students'][0])
print(course['students'][1])

"""
you can use in to check if key exists in dictionary
'hola' in translations # True
'bonita' in translations # False
"""

translations = {'hola':'hello', 'adios':'goodbye'}
answer = input('give me a word in spanish')
if answer in translations:
    print(translations[answer])
else:
    print('I don\'t know that word!')


import random

"""
treat the results of the rolls as the key
and the count as the value
{ 2: 300, 3:400, 4: 500}


creating a new key value pair
d[key_that_does_not_exist] = some_new_value
(no key error here, instead, new k/v pair)
"""
frequency = {}
for number_of_roll in range(1000):
    roll1 = random.randint(1, 3)
    roll2 = random.randint(1, 3)
    total = roll1 + roll2
    if total in frequency:
        frequency[total] += 1
    else:
        frequency[total] = 1

print(frequency)






























