"""
these are in the same folder
and i'm running them from that folder 

class04_modules.py
class04_myfunctions.py

this file imports class04_myfunctions
"""
import class04_myfunctions

print('this is a new file!!!!')

animals = ['cat', 'bat', 'dog', 'ant']

search = input('what are you looking for?')

if class04_myfunctions.in_list(search, animals):
    print('found', search)
else:
    print(search, 'not here! 404')

