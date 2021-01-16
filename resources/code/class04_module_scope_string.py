"""
optional module import syntax
returning nothing
scope
return multiple things from functions 
list methods
setting a value in a list
in / not in

calculate mean
"""
"""
import myfunctions
print('print from app', __name__)

"""
"""
from myfunctions import in_list
print(in_list(10, [1, 2, 3]))
"""
"""
from myfunctions import *
foo()
print(in_list(10, [1, 2, 3]))
"""
"""
where are variables available?

scope - the textual part of the program where you can use / have access to a variable
when something defined outside of functions, then it's in the global scope
that means that it can be used / accessed anywhere
"""

"""
score = 100

def print_score():
    # I have access to score
    # because score is global
    print(score)
print_score()
"""
"""
if i have something defined in a functions, it's only avaiable within that function
this variable is local to the function
"""


def greet(greeting, name):
    sentence = "%s %s" % (greeting, name)
    return sentence

greet('hello', 'joe')
print(sentence)

"""
def f():
    some_var = 1
    def g():
        some_name
"""
"""
imagine you have a function and in the function body you have a name
l local
e enclosing
g global
b built-in



def foo():
    print = "blah"
    print('hello')
"""
[2, 3, 4]
>>> for word in words:
...   print(word + '!!!!!')
...
foo!!!!!
bar!!!!!
baz!!!!!
qux!!!!!
corge!!!!!
>>> for character in "you may have guessed":
...   print(character)
...
y
o
u

m
a
y

h
a
v
e

g
u
e
s
s
e
d
>>> "%s is a %s" % ('Joe', "Human")
'Joe is a Human'
>>> # more human than human
...
>>> def selfish():
...   x = 1 + 2
...
>>> result = selfish()
>>> print(result)
None
>>> # None is a special value... it means that absence of a value
... # when a function doesn't explicitly return something with return statement
...
>>> result = print('hello')
hello
>>> print(result)
None
>>> result = int("23"
... )
>>> print(result)
23
>>> def generate_point():
...   return 2, 3, 4
...
>>> x, y , z = generate_point()
>>> x
2
>>>
>>> y
3
>>> def my_abs(n):
...   if n > 0:
...     return n
...   else
  File "<stdin>", line 4
    else
        ^
SyntaxError: invalid syntax
>>> def my_abs(n):
...   if n > 0:
...     return n
...   else:
...     return -n
...
>>> def problem():
...   return "is this ok?"
...   return "no it is not"
...
>>> print(problem())
is this ok?
>>>


















































