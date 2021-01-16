import random

sounds = ['beep', 'buzz', 'fizz', 'honk']
for i in range(20):
	print(random.choice(sounds)) 

print('-----')

random.shuffle(sounds)
for sound in sounds:
	print(sound)

