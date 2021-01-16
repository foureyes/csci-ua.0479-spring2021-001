from matplotlib import pyplot as plt
import numpy as np
"""
plt.plot([1, 2, 3], [1, 2, 3], 'go')
plt.plot([1, 2, 3],[1.5, 1.1, 2.5],  '-', color='#ff0000')
"""


import numpy as np

# our data
# ====



freq = {}

def remove_punc(s):
    new_s = ''
    for ch in s:
        if ch.isalpha() or ch == ' ':
            new_s += ch
    return new_s


with open('/tmp/pride.txt', 'r') as f:
    for line in f:
        clean_line = remove_punc(line)
        print('clean:', clean_line)
        words = clean_line.split(' ')
        for w in words:
            if len(w) > 0 and w[0].isupper():
                freq[w] = freq.get(w, 0) + 1
    print(freq)
            

sorted_keys = sorted(freq, key=freq.get)
sorted_vals = []
for k in sorted_keys:
    sorted_vals.append(freq[k])

words = sorted_keys[len(sorted_keys) - 10:]

# their arms (the y values)
num = sorted_vals[len(sorted_vals) - 10:]

# the x values (0, 1, or 2)
x = np.arange(len(words))
 
# plotting
# =====
plt.bar(x, num, align='center')
plt.xticks(x, words)
plt.ylabel('count')
plt.xlabel('word')
plt.title('count of words')
plt.show()
"""
import numpy as np
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
"""

"""
import numpy as np
x = np.arange(1, 101)
y = x ** 3
plt.plot(x, y, 'k-')
plt.xticks([0, 25, 50, 75, 100])
plt.yticks([0, 1000000], ['smol', 'extra'])
plt.show()
"""



