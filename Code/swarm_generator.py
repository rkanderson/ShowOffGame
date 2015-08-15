
# PURPOSE OF THIS GAME:
# To show that we the SHS Game Design Club mean buisness.
# All rights reserved.

import pygame
from pygame.locals import *
import main
from enemies import *

"""This file holds the SwarmGeneartor class, whose static
generate_swarm method will return an array of enemies based
on a given number. Swarms are like levels."""

pygame.init()

class SwarmGenerator:
	@staticmethod
	def generate_swarm(level, game):
		swarm = []
		if level==0:
			for row in range(3):
				for col in range(10):
					swarm.append(main.Enemy(game, (50+col*main.Enemy.width, row*main.Enemy.height)))
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

		#shift swarm to exist just outside of screen
		max_y = 0
		for enemy in swarm:
			if enemy.rect.bottom > max_y: max_y=enemy.rect.bottom
		for enemy in swarm:
			enemy.y-=max_y
		return swarm