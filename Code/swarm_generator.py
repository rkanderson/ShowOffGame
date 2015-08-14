
# PURPOSE OF THIS GAME:
# To show that we the SHS Game Design Club mean buisness.
# All rights reserved.

import pygame
from pygame.locals import *
from main import *
from enemies import *

"""This file holds the SwarmGeneartor class, whose static
generate_swarm method will return an array of enemies based
on a given number. Swarms are like levels."""

pygame.init()

class SwarmGenerator:
	@staticmethod
	def generate_swarm(level):
		swarm = []
		if level==0:
			
		elif level==1:
			pass
		elif level==3:
			pass
		elif level==4:
			pass
		elif level==5:
			pass
		elif level==6:
			pass
		else:
			print("@swarm_generator: I don't know what to give for that number.")
		return swarm