"""This modules tests decorated.py
"""
from decorated import debug
from decorated import count
from decorated import limit_one_call
try:
    from decorated import limit_calls
except:
    pass

def print_with_border(*args, **kwargs):
    """use in place of print to add a border around the output of what would
    regularly be printed:

    print_with_border("hello", "there")

    prints out...

    ###############
    # hello there #
    ###############
    """
    s = kwargs.get('sep', ' ').join(args)
    multiplier = max(len(line) for line in s.split('\n'))

    char = kwargs.get('char', '#')
    for k in ('char', 'sep'):
        if k in kwargs:
            del kwargs[k]

    border = (multiplier + 4) * char
    template = '{} {{:<{}s}} {}'.format(char, multiplier, char)
    template = '{}\n{}\n{}'.format(border, template, border)
    print(template.format(s), **kwargs)
 
print_with_border('TESTING DEBUG DECORATOR')

"""
testing debug with a custom function, foo
"""
@debug
def foo(a, b, c):
    return "bar"

foo([1, 2, 3], "hello", False)

print()

"""
creating a debugged version of a built-in function
"""
debugged_max = debug(max) 
m = debugged_max(99, 100)

print()

print_with_border('TESTING LIMIT_ONE_CALL DECORATOR')

"""
limiting say_hello to one call ()
"""
@limit_one_call
def say_hello():
    print("hello")

for i in range(3):
    print('calling decorated say_hello {}, output is:'.format(i))
    say_hello()

print()

print_with_border('TESTING COUNT DECORATOR')

"""
create a version of str that outputs how many times it was called
"""
counted_str = count(str)
res = counted_str(4)
res = counted_str(12)

print() 

@count
def say_goodbye():
    return "bye!"
res = say_goodbye()
res = say_goodbye()

print()

try:
    """limit say_hi_to_everyone to 2 calls"""
    @limit_calls(2)
    def say_hi_to_everyone(*args, greeting='hello'):
        """returns string consisting of greeting and arg for 
        every argument passed in
        """
        return '\n'.join(['{} {}'.format(greeting, name) for name in args])

    print_with_border('TESTING LIMIT_CALLS DECORATOR (EXTRA CREDIT)')

    print('value in __name__:', say_hi_to_everyone.__name__)
    print('value in __doc__:', say_hi_to_everyone.__doc__)
    for i in range(1, 4):
        print('call', i, '\n-----')
        res = say_hi_to_everyone('alice', 'bob', greeting='hi')
        print(res, '\n')
except NameError:
    pass
