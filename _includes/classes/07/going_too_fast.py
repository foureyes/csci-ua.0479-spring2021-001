speed_limit = int(input('What is the speed limit?\n> '))
speed = int(input("How fast are you goin'?\n> "))
if speed < speed_limit - 5:
	message = "You're going too slow!"
elif speed >= speed_limit - 5 and speed <= speed_limit + 5:
	message = "Your speed is just right!"
elif speed > speed_limit + 5:
	message = "You're going too fast!"
print(message)

