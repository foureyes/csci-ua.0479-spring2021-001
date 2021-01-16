"""
exceptions
tuples
dictionaries
questions about hw
sample of using dictionaries in a graphical application
file i/o
"""

"""
types of errors
=====
1. syntax
2. runtime errors... code is syntactically correct, but during run time it crashes
    * Exception
        * NameError ... you try to use an identifier that doesn't exist yet (variable name, func name, etc.)
        * TypeError ... trying to add int + str, or type is not mutable 
        * IndexError ... use an index that doesn't exist
        * ValueError 
        * ZeroDivisionError
    Traceback <-- generic term for finding out where error occured
3. logical error ... code runs fine, doesn't crash  ...but doesn't do what you want it do
"""
"""
try:
    # code that may cause an error goes here
    # if error occurs within try block
    # then execute code in except block
    # if there's no error skip except and resume
    # program after try/except block
except:
    # code that deals with error goes here
"""
"""
answer = input('give me number of inches')
if answer.isdigit():
    inches = float(answer)
    feet = inches / 12
    print("{} inches is {} feet".format(inches, feet))
else:
    print('nooope!')
"""
"""
answer = input('give me number of inches')
try:
    inches = float(answer)
    feet = inches / 12
    print("{} inches is {} feet".format(inches, feet))
except:
    print('sorry that was not a number!!!!')
"""    
#  of slices in a pie
"""
people = input("how many people are eating pizza?\n>")
try:
    n = int(people)
    print("Each person can have %s slices" % (8/n))
except ValueError:
    print('that wasn\'t a number')
except ZeroDivisionError:
    print('MOAR 4 ME!')

people = input("how many people are eating pizza?\n>")
try:
    n = int(people)
    print("Each person can have %s slices" % (8/n))
except:
    print('nope')

people = input("how many people are eating pizza?\n>")
try:
    n = int(people)
    print("Each person can have %s slices" % (8/n))
except Exception:
    print('nope')
"""
"""
choose a cup:
['O', 'O', 'O']
> 1
['O', '.', 'O']
you won!

choose a cup:
['O', 'O', 'O']
> 2
['O', '.', 'O']
you lost!

choose a cup:
['O', 'O', 'O']
> this is scam!!!!
['O', '.', 'O']
you still lose, it's def a scam!

choose a cup:
['O', 'O', 'O']
> 100
['O', '.', 'O']
you stil lose, that cup doesn't exist
"""
"""
create set of cups
place a coin in a random cup
user interaction
error handling
"""

"""
num = int(input('how many cups?'))
cups = []
for i in range(num):
    cups.append('O')
"""
"""
import random 
def generate_cups(n):
    cups = ['O'] * n
    # ask for input here...
    i = random.randint(0, len(cups) - 1)
    cups[i] = '.'
    return cups

def main():
    cups = generate_cups(3)
    try:
        answer = int(input('pick a cup 0,{}'.format( len(cups) - 1)))
        if cups[answer] == '.':
            print('you won!')
        else:
            print('you lost!')
        print(cups)
    except IndexError:
        print('that cup does not exist')
    except ValueError:
        print('that is not a number!!!')

main()
"""
"""
>>> ['hello'] * 3
['hello', 'hello', 'hello']
>>> animals = ['owl', 'cat', 'bat']
>>> import random
>>> random.choice(animals)
'cat'
>>> random.choice(animals)
'owl'
>>> random.choice(animals)
'bat'
>>> random.choice(animals)
'owl'
>>> animals
['owl', 'cat', 'bat']
>>> random.shuffle(animals)
>>> animals
['owl', 'cat', 'bat']
>>> random.shuffle(animals)
>>> animals
['cat', 'owl', 'bat']
>>>
"""
"""
>>> t = 1, 234
>>> t
(1, 234)
>>> print('hello', 'bye')
hello bye
>>> print(('hello', 'bye'))
('hello', 'bye')
>>> lonely = 'dog',
>>> lonely
('dog',)
>>> lonely = 'dog', ''
>>> a, b = 1, 2
>>> a
1
>>> b
2
>>> lonely
('dog', '')
>>> c, d = lonely
>>> c
'dog'
>>> d
''
>>> "%s is going to be a %s' % ('felix', 'ice cream cone')
  File "<stdin>", line 1
    "%s is going to be a %s' % ('felix', 'ice cream cone')
                                                         ^
SyntaxError: EOL while scanning string literal
>>> '%s is going to be a %s' % ('felix', 'ice cream cone')
'felix is going to be a ice cream cone'
>>> '%s is going to be ' % felix
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'felix' is not defined
>>> '%s is going to be ' % 'felix'
'felix is going to be '
>>> lonely
('dog', '')
>>> lonely[1] = 'cat'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> lonely.append('bat')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> len(lonely)
2
>>> lonely * 2
('dog', '', 'dog', '')
>>> for item in lonely:
...   print(item)
...
dog

>>> dir(lonely)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> lonely + ('owl', 'ant', 'eel')
('dog', '', 'owl', 'ant', 'eel')
>>> lonely
('dog','')
"""
"""
>>> points = [(3, 4), (10, 20), (100, 200)]
>>> points
[(3, 4), (10, 20), (100, 200)]
>>> for p in points:
...   print(type(p))
...
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
>>> for p in points:
...   print(p[0])
...
3
10
100
>>> for x, y in points:
...   print(x)
...
3
10
100
>>> words
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'words' is not defined
>>> animals
['cat', 'owl', 'bat']
>>> enumerate(animals)
<enumerate object at 0x10271c708>
>>> list(enumerate(animals))
[(0, 'cat'), (1, 'owl'), (2, 'bat')]
>>> for i, value in enumerate(animals):
...   print(i, value)
...
0 cat
1 owl
2 bat
>>> def gimme_two_things():
...   return 'thingy', 'something'
...
>>> a, b = gimme_two_things()
>>> a
'thingy'
>>> b
'something'
>>>
"""





































































