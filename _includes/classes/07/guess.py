import random
import sys
start, end = 1, 10
keep_playing = True 
secret_number = random.randint(start, end)
while(keep_playing):
	guess = int(input("I'm thinking of a number between 1 and 10; guess what it is!\n> "))
	if guess == secret_number:
		print("I was thinking of %s!.  You got it right!" % (secret_number))
		keep_playing = False
	elif guess > secret_number:
		print("Too high!")
	elif guess < secret_number:
		print("Too low!")
	
