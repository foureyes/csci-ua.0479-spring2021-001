"""
import matplotlib.pyplot as plt
y_vals = [2, 4, 6, 10, 12, 14]
# x vals [0, 1, 2, 3, 4, 5]
# default will always be blue solid line
plt.plot(y_vals)
plt.show()
"""
"""
import matplotlib.pyplot as plt
y_vals = [2, 4, 6, 10, 12, 14]
x_vals = [10, 11, 12, 13, 14, 15]
# default will always be blue solid line
plt.plot(x_vals, y_vals)
plt.show()
"""
"""
import matplotlib.pyplot as plt
y_vals = [2, 4, 6, 10, 12, 14]
x_vals = [10, 11, 12, 13, 14, 15]
# default will always be blue solid line
plt.plot(x_vals, y_vals, 'y--')
plt.show()
"""

"""
'rgbcmykw'
':-'
'--'
'v'
'+'
'o'
"""

"""
import matplotlib.pyplot as plt
y_vals = [2, 4, 6, 10, 12, 14]
y_vals2 = [1, 2, 3, 4, 5, 6, 7, 8, 15]
y_vals3 = [4, 4, 3, 4, 5, 4, 7, 4, 4]
# default will always be blue solid line
plt.plot(y_vals, 'k:')
plt.plot(y_vals2, 'g-')
plt.plot(y_vals3, 'y--')
plt.show()
"""
"""
import matplotlib.pyplot as plt
y_vals = [2, 4, 6, 10, 12, 14]
y_vals2 = [1, 2, 3, 4, 5, 6, 7, 8, 15]
y_vals3 = [4, 4, 3, 4, 5, 4, 7, 4, 4]
# default will always be blue solid line
plt.plot(y_vals, color='#ff0000', linestyle='dotted', marker='o')
plt.show()
"""
"""
numpy is:

a numerical computing library that allow for manipulation of vectors and matrices

scalar = 5
vector = [1, 2, 3]
matrix = [[1, 2, 3],
          [4, 5, 6]]

numpy array... vector or a matrix and LOOKS like a list

numpy arrays are MUCH faster than regular lists
functionality that is peculiar to working with data as arrays (vectors, matrices, etc.)
"""

"""
import matplotlib.pyplot as plt
import numpy as np
plt.plot([1, 2, 3, 4, 5, 5, 5], 
                [3, 4, 4, 2, 1, 2, 3])
plt.xlim(0, 7)
plt.ylim(0, 5)
plt.show()
"""

"""
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 101)
y = x ** 3
plt.plot(x, y, 'k-')
plt.xticks([0, 25, 50, 75, 100])
plt.yticks([0, 1000000], ['smol', 'extra'])
plt.show()
"""

import matplotlib.pyplot as plt
import numpy as np
animals = ['snake', 'human', 'octopus']
num_arms = [0, 2, 8]
x_vals = np.arange(0, len(animals))

plt.bar(x_vals, num_arms, align='center')
plt.ylim(0, 10)
plt.xticks(x_vals, animals)
plt.title('num of arms per animal')
plt.xlabel('animal')
plt.ylabel('arms')

# x coordinates - 0 ... num of animals
# the heights of the bars: num of arms
# labels for the x coordinates
plt.show()





























































