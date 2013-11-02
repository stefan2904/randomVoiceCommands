import os
import time
from random import randint

# Config:
speed 		= 0.2 # call a command every 'speed' seconds
commands 	= ["red", "blue", "purple"]

# Global vars:
counter = 0

def say(word):
	nr = randint(1,len(commands)*10) % len(commands)
	os.system("say " +commands[nr])

def say_random_command():
	say("red")

try:
	while True:
		say_random_command()
		counter += 1
		time.sleep(speed)
except KeyboardInterrupt:
			time.sleep(0.5)
			say("So we are done, you played " +str(counter) +" rounds! bye bye")
