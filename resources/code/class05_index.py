colors = ['blue', 'puce', 'dusty rose', 'fuscia']
# possible indexes
# 0, 1, 2, 3
"""
for i in range(len(colors)):
    print(i)
"""
"""
if you want to change the original list
OR if for some reason you need to the index
then loop with range instead
"""
"""
print('before', colors)
for i in range(len(colors)):
    colors[i] = colors[i] * 2
print('after', colors)
"""


"""
2 x ways to loop over list
for color in colors:
    ....

# use this for changing original list
# based on position
# maybe you need the index as part of your program
for i in range(len(colors):
    .... do stuff with i
"""

"""
for i in range(len(colors)):
    print(i + 1, colors[i])
"""

"""
for c in colors:
    # if you reassign loop variable
    # that will never change the original list
    c = c * 2
    # colors will remain the same
    # regardless of assignment that we do
    # to loop variable
    print(c)

print(colors)
"""


"""
snake = 'hissy elliot'


def shout():
    # local variable snake referenced before assignment 
    # creates a local ...
    snake = snake + "!"
    # assignment is not yet finished when we look up snake

    print('in function', snake)

shout()
print('out of function', snake)
"""
"""
snake = 'hissy elliot'
def shout():
    snake = "sir hiss-a-lot"
    print('in function', snake)

shout()
print('out of function', snake)
"""


"""
# we can change a mutable global variable
# from within a function
characters = ['yt', 'hiro protagonist', 'raven']

def remove_first():

    characters.pop(0)
    characters[0] = 1
remove_first()
print(characters)
"""
"""
characters = ['yt', 'hiro protagonist', 'raven']

def remove_first():
    # all this is doing is creating a new local variable
    # global doesn't change
    # when we do assignment in a function, it creates locals
    characters = []
remove_first()
print(characters)
"""
"""
# 1 lists are mutable
# 2 we're passing it in is a parameter

characters = ['yt', 'hiro protagonist', 'raven']


def remove_first(lst):
    lst.pop(0)

print('before', characters)
result = remove_first(characters)
print(result)
print('after', characters)
"""

"""
def double_every_element_in_place(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
    return numbers
    # no return

my_nums = [2, 4, 6]
print(my_nums)
result = double_every_element_in_place(my_nums)
print(result)
print(my_nums)
"""
"""

# idiomatic way of getting indexes in python
bands = ['lil yachty', 'migos', 'outkast', '21 savage']


for ele in bands:
   ...

for i in range(len(bands):
    ...

for i, ele in enumerate(bands):
    print(i, ele)
"""
"""
>>> 1, 2
(1, 2)
>>> [1, 2]
[1, 2]
>>>
>>> "1, 2"
'1, 2'
>>> 1, 2
(1, 2)
>>> (1, 2)
(1, 2)
>>> numbers = (1, 2, 3, 4)
>>> numbers * 2
(1, 2, 3, 4, 1, 2, 3, 4)
>>> numbers[0]
1
>>> for n in numbers:
...   print(n)
...
1
2
3
4
>>> a,b = 1, 2
>>> a
1
>>> b
2
>>> numbers
(1, 2, 3, 4)
>>> a, b, c, d = numbers
>>> d
4
>>> bands = ['joy division', 'zola jesus', 'cure']
>>> bands
['joy division', 'zola jesus', 'cure']
>>> list(enumerate(bands))
[(0, 'joy division'), (1, 'zola jesus'), (2, 'cure')]
>>> for t in enumerate(bands):
...   print(type(t), t)
...
<class 'tuple'> (0, 'joy division')
<class 'tuple'> (1, 'zola jesus')
<class 'tuple'> (2, 'cure')
>>> for t in enumerate(bands):
...   i, ele = t
...   print("%s - %s" % (i, ele))
...
0 - joy division
1 - zola jesus
2 - cure
>>> for i, ele in enumerate(bands):
...   print(i, ele)
...
0 joy division
1 zola jesus
2 cure
>>>

"""












































