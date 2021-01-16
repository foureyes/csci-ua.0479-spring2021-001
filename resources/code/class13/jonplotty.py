
import matplotlib.pyplot as plt
import numpy as np



"""
feels = {'👍': 5, '😒':3, '🍠':12}
plt.bar(np.arange(len(feels)), list(feels.values()), align='center', color='#aaddff')
plt.xticks(np.arange(len(feels)), list(feels.keys()))

plt.ylim(0, 14)
plt.ylabel('Votes')
plt.xlabel('Feels')
plt.title('How U Feel Abt This Graph?')
plt.show()
"""

"""
# labels
feels = ('👍', '😒', '🍠')

# y values
num_votes = [5, 3, 12]

# the x values (based on number of labels)
x = np.arange(len(feels))

plt.bar(x, num_votes, align='center', color='#aaddff')
plt.xticks(x, feels)

plt.ylim(0, 14)
plt.ylabel('Votes')
plt.xlabel('Feels')
plt.title('How U Feel Abt This Graph?')
plt.show()
"""
"""
import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 9, 16]
x2 = [0, 1, 2, 3, 4]
y2 = [4, 5, 6, 7, 8]

plt.plot(x, y, 'r--', x2, y2, 'b-')
plt.xticks([0, 2, 4], ['small', 'medium', 'large'])
plt.yticks([0, 16], ['not much', 'a lot'])
plt.xlabel('pizza size')
plt.ylabel('amount of toppings')
plt.xlim(-1, 5)
plt.ylim(0, 20)
plt.show()
"""


"""
# plt.style.use('ggplot')
# fivethirtyeight
# grayscale
# seaborn-muted
# seaborn-dark
# ggplot
# bmh

x = np.arange(0, 25)
y = np.array([(n * 4) ** 2 for n in x])
x2 = np.arange(0, 25)
y2 = np.array([n ** 3 for n in x2])

plt.style.use('ggplot')
plt.plot(x, y, 'r-', x2, y2, 'b:')
plt.plot(x + 2, y + 2, 'k-', x2, y2, 'g:')
plt.show()
"""

"""
import csv
with open('./resources/code/class13/populationbycountry19802010millions.csv') as f:
    csv = csv.reader(f)
    for row in csv:
        for item in row:
            print(item)
            """
"""
import csv
with open('./resources/code/class13/populationbycountry19802010millions.csv') as f:
    csv = csv.DictReader(f)
    for row in csv:
        print(row)
"""
"""
import csv
with open('./resources/code/class13/movies.csv') as f:
    csv = csv.DictReader(f)
    for row in csv:
        print(row)
"""
"""
import csv
with open('./resources/code/class13/populationbycountry19802010millions.csv') as f:
"""
"""
np.nan
def convert_to_numbers(vals):
    new_list = []
    for v in vals:
        try:
            new_list.append(float(v))
        except ValueError:
            new_list.append(np.nan)

    return new_list

def random_color():
    return np.random.random(3)

import csv
d = {}
with open('./resources/code/class13/populationbycountry19802010millions.csv') as f:
    csv = csv.reader(f)
    next(csv)
    for row in csv:
        d[row[0]] = convert_to_numbers(row[1:])
"""

"""
years = np.arange(1980, 2011)
plt.style.use('ggplot')
count = 0
for country, population in d.items():
    pct = (population[-1] - population[0]) / population[-1] 
    print(pct)
    if pct >= 0.67:
        plt.plot(years, population, color=random_color(), label=country)

    plt.plot(years, population, color=random_color(), label=country)
    if country in ['China', 'India', 'United States']:
        plt.plot(years, population, color=random_color(), label=country)

    print(country, years, population)
    if population[0] > 100:
        plt.plot(years, population, color=random_color(), label=country)

    print(country, years, population)
    if population[0] > 100:
        plt.plot(years, population, color=random_color(), label=country)

plt.legend(loc="upper left")
plt.show()



print(d)
"""
"""
x = np.arange(0, 25)
y = np.array([(n * 4) ** 2 for n in x])
x2 = np.arange(0, 25)
y2 = np.array([n ** 3 for n in x2])

plt.style.use('seaborn-dark')
plt.plot(x, y, 'r-', label='tears of joy')
plt.plot(x2, y2, 'b:', label='face with no good gesture')
plt.legend(loc="upper center")
plt.show()
"""

"""
feels = {'👍': 5, '😒':3, '🍠':12}
plt.style.use('ggplot')
plt.pie(list(feels.values()), labels=list(feels.keys()), autopct='%.2f%%')
plt.axis('equal')
    
plt.show()
"""
"""
edible_pies = ['Strawberry', 'Apple', 'Chocolate', 'Humble']
numbers = [2, 3, 4, 1]
plt.style.use('ggplot')
plt.pie(numbers, labels=edible_pies, autopct='%.2f%%', explode=[0, 0, 0, 0.1], colors=['#ffff00', (1, 0, 0), 'k', 'green'])
plt.title('number of pies eaten')
plt.axis('equal')
    
plt.show()
"""

"""
plt.plot([0, 2, 4, 9, 16], color=(0.5, 0.75, 1))
plt.show()
"""
"""
y1 = np.arange(0, 10);
y2 = np.arange(15, 5, -1)
plt.style.use('seaborn-notebook')

plt.subplot(221)
plt.plot(y1, 'bo')

plt.subplot(222)
plt.plot(y2, 'k')

plt.subplot(223)
plt.bar([0, 1, 2], [5, 2, 7])

plt.subplot(224)
plt.pie([70, 10, 30], explode=[0, 1, 0])
plt.axis('equal')

plt.show()
"""

"""
y = [3, 2, 2, 2, 2, np.nan, np.nan, 2, 2, 2, 1]
plt.style.use('seaborn-dark')
plt.plot(y, 'b-')
plt.show()
"""

