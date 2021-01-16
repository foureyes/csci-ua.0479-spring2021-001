"""
get_first_word(s)
param s: that string is a sentence, and we assume that every word in a sentence is separated
by a space

return the first word in a sentence


get_first_word("hello world") # gives back hello

if there are no space, then just return entire sentence (including if it's only empty string)
get_first_word("world") # gives back world
get_first_word("") # gives back ""
"""
"""
when we write a function, we're not necessarily asking for user input

all we want is a black box that may have parameters (inputs), and may have a return value (output)
"""

"""
def get_first_word(s):
    word = ''
    for ch in s:
        if ch == ' ':
            break
        else:
            word = word + ch
        # if we break after accumualting
        # we end up adding extra space

    return word
print(get_first_word('joe has a cat'))
print(get_first_word('patrick'))
"""
"""
find index of space
slice from start to index of space
return val
"""

"""
def get_first_word(s):
    add_last_letter = True
    for i in range(len(s)):
        if s[i] == ' ':
            add_last_letter = False
            break
        
    if add_last_letter:
        return s[0:i + 1]
    else:
        return s[0:i]


print(get_first_word('joe has a cat'))
print(get_first_word('rebekah'))
"""

"""
def letter_in_word(letter, word):
    for ch in word:
        if ch == letter:
            return True
    return False

print(letter_in_word('c', 'cat')) # true
print(letter_in_word('a', 'cat')) # true
print(letter_in_word('x', 'cat')) # false
"""


def remove_vowels(s):
    new_s = ''
    #vowels = ['A', 'E', ....]
    vowels = 'aeiouAEIOu'

    for ch in s:
        if ch not in vowels:
            new_s += ch
    return new_s

        #if ch == 'A' or ch == 'E' ...

    
remove_vowels('Picard') """ Pcrd """

"""
remove_vowels
accepts a string as a parameter
returns a string without any vowels in it
hint: build a string by accumulating characters
hint: we just looked in and not in 
"""
"""
>>> title.
KeyboardInterrupt
>>> title.index("e")
4
>>> title.find("q")
-1
>>> title.index("q")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> w
'\t\t\t\thello\n\n\n\\world'
>>> print(w)
               hello


\world
>>> w.strip()
'hello\n\n\n\\world'
>>> template = "{} my name is {}"
>>> template.format('hello', 'joe')
'hello my name is joe'
>>> template = "{2} my name is {1}"
>>> template.format('hello', 'joe')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> template = "{1} my name is {0}"
>>> template.format('hello', 'joe')
'joe my name is hello'
>>> template = "{1} my name is {0} {1}"
>>> template.format('hello', 'joe')
'joe my name is hello joe'
>>> template = "{greeting} my name is {name}"
>>> template.format(greeting='hello', name='joe')
'hello my name is joe'
>>> t = 'hola'
>>> template.format(greeting=t, name='joe')
'hola my name is joe'
>>> template = "{greeting} {greeting} my name is {name}"
>>> template.format(greeting=t, name='joe')
'hola hola my name is joe'
>>> greeting='hola'
>>> template.format(greeting, name='joe')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'greeting'
>>> template.format(greeting=t * 3, name='joe')
'holaholahola holaholahola my name is joe'
>>>
"""














































"""
print(get_first_word('joe has a cat'))
print(get_first_word('patrick'))
"""


























