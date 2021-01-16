
"""
import random

def generate_unique_numbers(how_many):
    numbers = []
    while len(numbers) < how_many:
        n = random.randint(1, 59)
        if n not in numbers:
            # this is not that great...
            numbers.append(str(n))
    return numbers

new_file = open('luckynumbers.txt', 'w')
new_file.write('lucky numbers\n')
numbers = sorted(generate_unique_numbers(5))
new_file.write('\n'.join(numbers))
new_file.close()
"""

"""
# a file object is an iterable object
# one way to read a file is to loop over the file object
# every line as the loop variable
file_obj = open('luckynumbers.txt', 'r')
for line in file_obj:
    print(line.strip())
"""
"""
file_obj = open('luckynumbers.txt', 'r')
# gives us a list, every element in list is a line in the file
lines = file_obj.readlines()
print(lines)
"""

"""
file_obj = open('luckynumbers.txt', 'r')
# gives us entire contents as a string
content = file_obj.read()
print(content)
"""
file_write = open('doubled.txt', 'w')

file_obj = open('luckynumbers.txt', 'r')
for line in file_obj:
    file_write.write((line.strip() * 2) + '\n')

file_write.close()
file_obj.close()





































