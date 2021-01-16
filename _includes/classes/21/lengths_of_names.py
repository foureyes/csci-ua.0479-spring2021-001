names = input('some names plz, separated by commas\n>')
for name in names.split(','):
	n = name.strip()
	print('%s has %s letters in it' % (n, len(n)))
