""" pastry buying guide """

day = input("What day is it (ex Thursday, Friday, etc.)?\n> ")
time = int(input("What time is it (in 24 hour time)?\n> ")) # not adventure
delicious_time = 16
if day == 'Friday':
	if time >= delicious_time:
		print("Go ahead, you deserve a treat") 
	else:
		print("Just wait %s more hours" % (delicious_time - time)) 
else:
	print("Don't do it!  Just don't.")
