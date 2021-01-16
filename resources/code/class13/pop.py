import matplotlib.pyplot as plt
import numpy as np

def convert_to_floats(list_strings):
    new_list = []
    for val in list_strings:
        try:
            new_list.append(float(val))
        except ValueError:
            new_list.append(np.nan)
    return new_list


#populationbycountry19802010millions.csv
import csv
d = {}

with open('/tmp/populationbycountry19802010millions.csv', 'r') as f:
    reader = csv.reader(f)
    # consume the header / eliminate the header
    next(reader)
    for row in reader:
        country = row[0]
        # we have to convert to floats
        # --, N/A converted to np.nan
        # country is first, and values are after
        pop_by_year = convert_to_floats(row[1:])
        d[country] = pop_by_year

print(d)

years = np.arange(1980, 2011)
plt.style.use('ggplot')
for country, pops in d.items():
    rate = (pops[-1] - pops[0]) /  pops[-1]
    if rate > 0.7:

        # print(country, pops)
        # color = (random.randint())
        color = np.random.random(3)
        plt.plot(years, pops, color=color, label=country)

plt.legend(loc='upper left')


plt.show()
"""
# x coords????
# years
years = np.arange(1980, 2011)

# y coords
d['country name'].values()

# legend label
'country name'
"""




















