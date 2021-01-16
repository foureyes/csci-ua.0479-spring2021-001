"""
if you want to execute different pieces of code
based on some condition (conditionally execute)....
use an if statement
"""
"""
if some_boolean_expression:
    code_to_run_if some_boolean_expression is true
1. keyword if
2. boolean expression ... an expression that gives back a boolean value (True or False) ex. 5 == 2
    answer == 'Yes'
3. end that with a colon
4. new line
5. single indent
6. code that should be executed if boolean expression is true
    more than one line, as long as they're indented

as long as i have indented code
that is considered in the same "block" of code
to be executed if cond is true
once we "de"-indent, then we're out of the block
"""
"""
answer = input('do you want some cake\n>')
if answer == 'yes':
    print('here, have some cake')
    print('I am still here')

print('done')
"""
"""
if else statement
chooses between 2 blocks of code
only one will get executed
using else:

else always needs an if before it
don't indent else
follow it by a colon
aaaand.... an indented block of code
"""
"""
answer = input('do you want some cake\n>')

if answer == 'yes':
    print('here, have some cake')
else:
    print('no cake 4 u')

"""
"""

answer = input('what is 2 to the 4th power?\n>')
if int(answer) == 2 ** 4:
    print('yup, you got it!')
else:
    print('close, but no cigar!')
"""
"""
answer = int(input('please enter a secret num'))

if answer == 5:
    print('you got it')
else:
    print('you are wrong')
"""
"""
 p | q | p or q and o
----------------
 f | f | f
 f | t | t
 t | f | t
 t | t | t



evaluate all parens
numeric and string operators (pemdas)
comparison operators
logical operators
	not
	and 
	or

not (8 != 8) or not True 
not False or not True 
True or False
True

"hello" == "world" or 5 + 5 > 8 and 4 * 3 < 16 and 28 != 0
"hello" == "world" or 5 + 5 > 8 and 12 < 16 and 28 != 0
"hello" == "world" or 10 > 8 and 12 < 16 and 28 != 0
False or 10 > 8 and 12 < 16 and 28 != 0
False or True and 12 < 16 and 28 != 0
False or True and True and 28 != 0
False or True and True and True
False or True and True
False or True
True
"""

"""
True or (8 > 2 and x == y)
"""
""""
answer = input('do you want some cake?')
if answer == 'yes':
	print('have some cake')

if answer == 'maybe':
	print('idk, ok!')

if answer != 'yes' and answer != 'maybe':
	print('no cake 4 u')
"""

    


"""
if answer == 'yes':
	print('have some cake')
else:
	if answer == 'maybe':
		print('idk, ok!')
	else:
		print('no cake 4 u')

"""

"""
same as if
but...
elif some_condition
and continually add more conditions
the first condition that evaluates to true
will have its block executed
all other blocks will be skipped
if none of the elifs evaluate to true
then execute else if it's present (else is optional)
"""

"""
answer = input('do you want some cake?')
if answer == 'yes':
	print('have some cake')
elif answer == 'maybe':
	print('idk, ok!')
elif answer == 'something else':
	print('????')
else:
	print('no cake 4 u')
"""






































