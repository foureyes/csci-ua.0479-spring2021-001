colors = ['red', 'green']
colors.append('blue')
print(colors)

colors = ['red', 'green']
more_colors = ['blue', 'orange']
colors.append(more_colors)
print(colors)

colors = ['red', 'green']
more_colors = ['blue']
colors.append(more_colors)
print(colors)

colors = ['red', 'green']
more_colors = ['blue', 'orange']
colors.extend(more_colors)
print(colors)
