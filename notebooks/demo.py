"""
what if delimiter (,) is part of actual data? quote it? do you double ,,
does it include the header
are there missing values
what is the encoding (hopefully  utf-8)
"""
with open('starbucks_drinkMenu_expanded.csv', 'r') as f:
    next(f)
    count = 0
    for line in f:
        line_parts = line.split(',')
        if int(line_parts[3]) > 200:
            print(line_parts[1], line_parts[3])


