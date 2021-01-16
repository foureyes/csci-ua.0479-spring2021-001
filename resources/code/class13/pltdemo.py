# always import
import matplotlib.pyplot as plt
import numpy as np

# plotting????
#x = [0, 1, 2, 3, 4]
#y = [0, 1, 2, 3, 4]
#stringformat = 'r:'
# single letters: b... blue, k black, r red, etc.
# line style o: circle marker, :: dots, --: dashed line, -: solid line, etc.
# matplotlib python3 pyplot.plot
#plt.plot(x, y, stringformat)

#plt.plot([0, 1, 2, 4, 9, 16], 'kv')

#plt.plot([0, 1, 2, 4, 9, 16], 'kv', [0, 1, 2, 3, 4], 'r-')

#plt.plot([0, 1, 2, 4, 9, 16], 'kv')
#plt.plot([5, 4, 3, 2, 1, 0] )
#plt.plot([0, 1, 2, 4, 9, 16], 'kv', [0, 1, 2, 3, 4], 'r-', [2, 2, 2, 2, 2, 2], 'g:')
"""
plt.plot([5, 4, 3, 2, 1, 0], color='#00ff00')
plt.xlabel('number of hours')
plt.ylabel('my energy')
plt.title("joe's energy throughout the day")
plt.xticks([0, 2, 5], ['early', 'afternoon', 'late'])
plt.yticks([0, 5], ['low', 'high'])
plt.xlim(0, 6)
plt.ylim(0, 10)
"""
"""
bar graph... the x coordinates of the edges of each bar
heights of every bar
these lists (or arrays) should be the same length
"""
"""
import numpy as np

feels = ('👍', '😒', '🍠')

num_votes = [5, 3, 12]

x = np.arange(len(feels))

plt.bar(x, num_votes, align='center')

plt.xticks(x, feels)

plt.ylim(0, 14)
plt.title('how u feel abt this graph')
plt.xlabel('feels')
plt.ylabel('votes')

"""
"""
import numpy as np

plt.style.use('ggplot')
plt.plot(np.arange(10), color=(0.0, 0.5, 1), label='cloud rap')
plt.plot([5, 5, 5, 5, 5, 5, 5, 5, 5], color='red', label='trap')
plt.legend(loc='upper left')

plt.show()
"""
"""
edible_pies = ['Strawberry', 'Apple', 'Chocolate', 'Humble']
numbers = [2, 3, 4, 1]

plt.style.use('ggplot')
plt.pie(numbers, 
        explode=[0, 0, 0, 0.5], 
        labels=edible_pies, 
        colors=['red', '#ffff00', (0, 1, 0), 'b'], 
        autopct='%.1f%%')
plt.axis('equal')

plt.show()
"""
y1 = np.arange(0, 10);
y2 = np.arange(15, 5, -1)
plt.style.use('ggplot')




# switch to subplot 1 in subplot with 2 rows
plt.subplot(3, 2, 1)
plt.plot(y1, 'bo')

# switch to subplot 2 in subplot with 2 rows
plt.subplot(3, 2, 2)
plt.plot(y2, 'k')

plt.subplot(9, 2, 3)
plt.pie([2, 5, 10, 12], explode=[0, 0, 1, 0])

plt.subplot(3, 2, 4)
plt.plot([7, 6, 8, 6, 7, 7], 'r:')
plt.show()




"""
header
=====

* this is item 1
* this is item 2

> i quoted this from u
"""









