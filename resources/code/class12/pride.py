"""
find all proper nouns (ok to be sloppy)
count 'em
graph the top 10 proper nouns
which character is mentioned 

Elizabeth
Darcy
Bennett

with will create a block of code
where some variable will be available
and when that block is exited
some "clean up" will be done

in example of with... when we open file
once, we're out of with, file is automatically closed
for you
"""

def remove_punc(s):
    new_s = ''
    for ch in s:
        if ch.isalpha() or ch == ' ':
            new_s += ch
    return new_s

# the counts of the words
freq = {}

with open('/tmp/pride.txt', 'r') as f:
    for line in f:
        clean_line = remove_punc(line).strip()
        words = clean_line.split(' ')
        for w in words:
            # if first letter is uppercase
            # this is short circuit evaluation
            # ignore 2nd part of and if first part is false
            if len(w) > 0 and w[0].isupper():
                # w is the word we're looking at
                # which we'll use as a key
                freq[w] = freq.get(w, 0) + 1
                """
                # how do know if we should set to 1 vs add 1
                freq[w] = 1
                freq[w] += 1
                """
    print(freq)

# sorted will return a new list of sorted elements
# key specifies how its its sorted
sorted_keys = sorted(freq, key=freq.get)

sorted_values = []

for k in sorted_keys:
    sorted_values.append(freq[k])

# loop over sorted keys
# get value associated with that key from dictionary
# push / append onto new sorted values
# now we have a sorted array of vals as well




# we can get a list of sorted keys from this dict
# by calling sorted

# only get top 10
sorted_keys = sorted_keys[-10:]
sorted_values = sorted_values[-10:]

print(sorted_keys)
print(sorted_values)


import matplotlib.pyplot as plt
import numpy as np
# these are the words: sorted_keys
# the x coords are arange(len(sorted_keys))
# these are the height: sorted_values
x_vals = np.arange(0, len(sorted_keys))

plt.bar(x_vals, sorted_values, align="center")
plt.xticks(x_vals, sorted_keys)

plt.show()





























































