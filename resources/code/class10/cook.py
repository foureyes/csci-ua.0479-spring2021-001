"""
fread = open('ingredients.txt', 'r')

# write will overwite an existing file
# if file doesn't exist, it'll create it
fwrite = open('double.txt', 'w')

for line in fread:
    line = line.strip() # removes
    # leading and trailing white space
    # spaces, tabs, newlines at the
    # beginning or end of a string
    parts = line.split(':')
    #fwrite.write(2 * int(parts[0]) + parts[1])
    fwrite.write("{}:{}\n".format(2 * int(parts[0]), parts[1]))

fread.close()
fwrite.close()

"""
fread = open('ingredients.txt', 'r')
#lines = fread.readlines()
#print(lines)

"""
content = fread.read()
print(content)
"""
"""
line = fread.readline()
print(line)
line = fread.readline()
print(line)
"""








"""
readlines
read
readline
"""










