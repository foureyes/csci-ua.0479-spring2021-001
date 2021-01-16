# go over some of the "old" slides
# try a sample "quiz" question(s) ... practice for the upcoming
# field some homework questions
# go over strings
# or go over more intermediate level stuff w/ lists


"""

>>> def foo(bar):
...
"""     

"""foo will print out the argument passed in"""

"""
...     print(bar)
...
>>> help(foo)

>>> # docstrings


is_leap_year...
"""
# call the function
# print out the result
# does the result match my expectation
# call the function twice

# automatically test the observed result vs your expected result
# assert statement
# assert boolean expression, "description"


# assert oberved == expected, "description of the test"

"""
def is_short_string(s):
    return len(s) < 3
    #return True

assert is_short_string('hello') == False, "this test determines if function returns false if we have a long string"
assert is_short_string('') == True, "returns true if string is less than 3 chars"
"""

"""
designing functions
create a chart called input, output and processing
input - what are the parameters?
output - what's the return value (NOT WHAT IS PRINTED)
processing - what goes in the body

my_abs <--
input:
    * a number
output:
    * a number, the absolute value of the input
processing
    * whatever calculation you have to make
"""

"""
in the doc string
is_leap_year(y)

y: int - the year used to determine if leap year our not
return: bool - True or False depending on if year is leap year
processing:
    describe the algo you might use
"""

"""
the most common case for no params is a main
"""

"""
def main():
    name = input('what is your name?')
    print(name)

main()
"""

"""
def foo():
    s = "bar"
    # no return 

result = foo()
print(result)
"""


# if there's no return, then function gives back None
# None is a special value that means NO VALUE


result = print('hello') # print does not return anything!!!! <-- None
print(result)

"""
def print()
    show something on screen
    but don't return anything
"""


# hello
# None
# it will def print out None

















































































