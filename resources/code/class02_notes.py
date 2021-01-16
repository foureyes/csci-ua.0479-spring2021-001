"""
print always prints out an ending of \n
you can change that by adding 
"keyword" argument to the arguments that you pass in
end="*"

by default, the separator between arguments passed in
is space
to change it... 
sep=""
"""
"""
print("hello", "patrick", "and", "sanjana", sep=" see this! ")
print("one", end="*")
print("two", end="*")
"""
"""
print
type
str
int
float
help
input
"""
"""
format
always returns a string
2 parameters:
    * the thing you want formatted (any value)
    * the way you want it formatted (in a string)

format specifier mini language
the number of decimal places in a floating point number
the total width of the string returned
"""
"""
x = 1
formatted_number = format(x, '>10.2f')
print(formatted_number)
"""

"""
times = 2
print('foo' + times * '!')
print('bar' + times * '!')
print('baz' + times * '!')
print('qux' + times * '!')
"""
"""
multiple assignment
"""
"""
a, b = 3, 4
print(a)
print(b)
"""
"""
a = 3
b = 21
"""

"""
# don't just do this
# imagine that you don't the values of a and b
# (they came from user input or from a file)
b = 3
a = 21
"""
"""
b = 3
a = 21
#swap values idiomatically in python
a, b = b, a
print('a', a)
print('b', b)
"""
"""
b = 3
a = 21
c = a
a = b
b = c
print('a', a)
print('b', b)
"""

"""
what is the name of the item? python plush toy
how much does it cost? 5
how many were purchased? 2
how much was paid? 12
(80 wide)
====================================================================
python plush toy x 2                                          $10.00
amount paid                                                   $12.00
change given                                                   $2.00
====================================================================
"""


# gather user input
item_name = input('what is the name of the item?')
cost = float(input('how much does it cost?')) 
quantity = int(input('how many were purchased?')) 
paid = float(input('how much was paid?'))

# total width of receipt
receipt_width = 70

# formatting specifiers
money_format = '.2f' # format as 2 decimal places
left_format = '<35s' # total width of string is 40 for left hand column
# the default sep is space
# so the total width is 70
# which 35 + 1 + 34, with 1 coming from the space
right_format = '>34s' # total width of money (right column)

total = cost * quantity
change = paid - total

# our actual receipt
print(item_name, cost, quantity, paid)
print('=' * receipt_width)

total_formatted = format('$' + format(total, money_format), right_format)
print(format(item_name + ' x ' + str(quantity), left_format), total_formatted)
paid_formatted = format('$' + format(paid, money_format), right_format)
print(format('amount paid', left_format), paid_formatted)
change_formatted = format(format('$' + format(change, money_format), right_format))
print(format('change given', left_format), change_formatted)




















































































