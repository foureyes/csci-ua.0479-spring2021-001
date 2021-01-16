count = 1
num = int(input("Enter a number\n>"))
while count ** 2 < num:
	print(count ** 2)
	count += 1
print(str(count) + " squares found")
