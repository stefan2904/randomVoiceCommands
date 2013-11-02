import sys
import os
import time
from random import randint

# Config:
speed 		= 0.4 # call a command every 'speed' seconds
commands 	= ["red", "blue", "purple"]

# Global vars:
counter = 0

def say(word):
	print word
	os.system("say " +word)

def say_random_command():
	nr = randint(1,len(commands)*10) % len(commands)
	say(commands[nr])

def handle_args():
	prog = sys.argv[0]
	global speed
	if len(sys.argv) < 2:
		print "no speed argument found, asuming speed=", speed
		print "to set speed, start program like this:"
		print prog, "<speed>"
	else:
		speed = float(sys.argv[1])
		print "running", prog, "with speed=", speed

# main:

handle_args()

try:
	while True:
		say_random_command()
		counter += 1
		time.sleep(speed)
except KeyboardInterrupt:
			time.sleep(0.5)
			
say("So we are done, you played " +str(counter) +" rounds! bye bye")
