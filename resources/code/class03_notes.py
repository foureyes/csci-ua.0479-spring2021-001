"""
% operators is yet another string operator
(kind of like * or +)
it evaluates to a string

allows the creation of "template" string
and... subs variables for placeholders in template

%s is the placeholder
% is the operators (takes two operands)

1. left hand side is the template
2. right hand side is comma sep vals that go into template

"Hello my name is %s" % "Joe"
'Hello my name is Joe'
"""
"""
name = 'Joe'
num = 9
animal = 'aardvark'
template = "My name is %s. I have %s %ss"
print(template % (name, num, animals))
print("My name is " + name + ". I have " + str(num) + " " + animal)

"""
"""
x = 1
delta = 1
print(x)
x = x + delta
print(x)
x = x + delta
print(x)
x = x + delta
print(x)
x = x + delta
print(x)
x = x + delta
"""
"""
1. condition controlled loop
2. count controlled loop (you can simulate count controlled with condition)

loop - repeated execution of a block of code
a single iteration - one repetition of a loop
"""
"""
while loops are condition controlled

1. keyword while
2. followed by a boolean expression, then colon
3. an indented block of code (that repeats as long as boolean expression is true)

code in block will be executed
then condition condition is checked
if cond is true, then repeat block, otherwise end loop

"""


"""
# prints out hello forever
# ctrl + c will stop infinite loop
while True:
    print('hello')
"""

"""
# nothing is printed because cond is false
while 1 == 'hello':
    print('hello')
"""

"""
# loops once because 
# flag is changed to false
# after 1st iteration
flag = True
while flag:
    print('hello')
    flag = False
print('Done')
"""
"""
when there's a condition that checks a variable to determine whether a loop
should continue or not, that variable is called a sentinal variable

if you want a while loop to stop,
at some point in time, the condition has to become false

1. have some variables (state) outside of the while loop
2. make your condition based on that variable(s) (state)
3. within your loop, modify or mutate that variable(s)


var = ...
while var > 0:
    change variable eventually so that it's not greater than 0
"""
"""
x = 1
delta = 1
print(x)
x = x + delta
print(x)
x = x + delta
print(x)
x = x + delta
print(x)
x = x + delta
print(x)
x = x + delta
"""
"""
# counts 1 through 5 by ones
count = 1
while count <= 5:
    print(count)
    count = count + 1
"""
"""
# count 2 through 8 by 2's
count = 2
while count <= 8:
    print(count)
    count = count + 2
"""
"""
continually ask the user if they want cake
until they say yes or yeah <-- this is when it stops

want some cake?
no
want some cake?
NOPE!
want some cake?
yes
"""

""" stop if the answer is either yes or yeah"""
""" keep on going as long as its not both yes and yeah"""

"""
# either use python tutor to see what the variables are
# step through line by line and evaluate the boolean expression yourself
# imagine answer was yes
# that means .... the boolean expression evaluates to False if we use and
# that means .... the boolean expression evaluates to True if we use or (because or
# only needs one True for the whole expression to be True)
answer = ''
while answer != 'yes' and answer != 'yeah':
    answer = input('want some cake?')
"""

"""
ask if you want to continue
and if you say no NO N it'll stop
"""

"""
These two boolean expressions are not equivalent
when you use a value in a boolean context (the op expects booleans)
then... it'll convert that value to a boolean:
"" (empty string) - False
0 - False
None
[]
"""

"""
everything else is True

answer == 'no' or answer == 'NO' or answer == 'N'
answer == 'no' or 'NO' or  'N'
"""
"""
>>> bool("hello" and "hello")
True
>>> bool("" and "hello")
False
>>> "hello" and "hello"
'hello'
>>> "hello" or ""
'hello'
>>> 0 or "what am i talking about"
'what am i talking about'
>>> 0 and "ok"
0
>>> "truthyyyyy" and "ok"
'ok'
>>>
"""
"""
total = 0

while True:
    answer = int(input('give me a num!!!'))
    total = total + answer
    print('current total is %s' % (total))
"""

"""
#what data are we keeping track of
total = 0
count_of_numbers = 0
answer = 'yes'

while answer == 'yes':
    print('Current total %s: ' % total)
    print('Numbers summed %s: ' % count_of_numbers)
    n = int(input('Give me a number to add\n>'))
    total += n
    count_of_numbers += 1
    answer = input('Do you want to continue?\n>')

average = total / count_of_numbers
print(average)
"""
"""
count controlled loop
it's a for loop
a for loop will go over every element in a collection of elements
is goes over every object in an iterable object


by collection i mean:

    a series (range) of numbers: 0, 1, 2, 3, 4
    2, 4, 6, 8

    a list: ['hello', 'bye', 'adios']

    a string: 'hello'

1. keyword for
2. the name of a variable (Whatever you want it to be) followed by in
3. an iterable object (a collection of things)
4. colon
5. indented block of code to repeat

a for loop will repeat block of code for every element in collection
(every thing in an iterable object)
within the body of the loop, the loop variable is available to be used
and it holds the current element being iterated over

iterable object:
    an object composed of other objects
    that has ability to return each element / item one at a time
"""
"""
names = ['finn', 'jake', 'pb']
for name in names:
    print(name)

animal = 'narwhal'
for letter in animal:
    print(letter)
"""
"""
a range object is an arithmetic sequence of numbers
and it's created by calling the range function


range can take three arguments
1. the start (starts with this number, including)
2. stop (goes up to this number, but doesn't include it)
3. step

two arguments
1. start - inclusive
2. stop - exclusive

step by default will be 1

one argument
1. stop - exclusive

start will be 0 by default
step by default will be 1

the preferred way to loop x number of times is simply

for some_var in range(x):
    print(some_var)
"""
"""
for i in range(10):
    print(i)
"""

"""
with a negative step, you go backwards
"""
"""
for num in range(100, 0, -1):
    print(num)
"""
"""
#prints nothing
for num in range(100, 0):
    print(num)
"""
"""
fizz buzz
prints out the numbers 1 through a 100
however
if number is divisible by 3 it'll print out fizz instead of num
if it's divisible by 5 it'll print out buzz instead of num
if it's divisible by both 3 and 5 it'll print out fizzbuzz instead of num

1
2
fizz
4
buzz
fizz
.
14
fizzbuzz
16
.
.
.
"""
"""
for num in range(1, 101):
    # may want to put narrowest condition up top
    if num % 5 == 0 and num % 3 == 0:
        print('fizzbuzz')
    elif num % 5 == 0:
        print('buzz')
    elif num % 3 == 0:
        print('fizz')
    else:
        print(num)
"""
"""
simple form of input validation is just using if

if passes_some_test
    code for rest of program goes here
else
    end program immediately with some message

if passes_some_test
    set the variable to that value
else
    set variable to default value


while input is not valid
    ask again
    (until we get valid input)
"""

"""
if you get a syntax error, but the line looks good
that means that some line above it is not syntactically correct
(that will typically be unbalanced parens or quotes)
"""
"""
if the user entered p ... or c
print that's valid
"""

"""
answer = input('please enter only p or c')
# if answer == 'p' or 'c':
# if answer == 'p' or True
if answer == 'p' or answer == 'c':
    print('that is valid!')
"""



"""
break - stop the loop completely
continue - goes on to the next iteration of the loop
"""

"""
# this will stop loop immediately (that means:
# 0 1 2 3 4 (Each on its own line)
for i in range(10):
    if i == 5:
        break
    print(i)

# essentially skip 5 because continue immediately goes to next iteration of loop
for i in range(10):
    if i == 5:
        continue
    print(i)
"""






































































































































































