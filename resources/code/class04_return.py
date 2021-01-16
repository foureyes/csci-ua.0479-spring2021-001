"""
return is a statement
a value has to be on the right hand side
that value can be an expression (that will be evaluated before the return)
and it does 2 things:
    * immediately stops the function
    * gives back the value / expression to the right of it
return statements have to be in a function
they can be in a loop, as long as that loop is in a function
"""

"""
def experiment():
    print(1)
    return 'foo'
    print(2)
experiment()
"""

"""
def experiment():
    for i in range(5):
        return i
print(experiment())

# function ends on first iteration!
"""

"""
def experiment():
    for i in range(5):
       print(i)
    # after the for loop, i will still refer to its last value
    return i
print('out of function', experiment())
"""










