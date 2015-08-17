
# PURPOSE OF THIS GAME:
# To show that we the SHS Game Design Club mean buisness.
# All rights reserved.

import pygame
from pygame.locals import *
import enemies

"""This file holds the SwarmGeneartor class, whose static
generate_swarm method will return an array of enemies based
on a given number. Swarms are like levels."""

pygame.init()

class SwarmGenerator:
	@staticmethod
	def generate_swarm(level, game):
		swarm = []
		print("Creating swarm id"+str(level))
		if level==0:
			for row in range(3):
				for col in range(10):
					swarm.append(enemies.Normal(game, (50+col*enemies.Enemy.width, row*enemies.Enemy.height)))
		elif level==1:
			for row in range(2):
				for col in range(10):
					swarm.append(enemies.Normal(game, (50+col*enemies.Enemy.width, row*enemies.Enemy.height)))
			swarm.append(enemies.Shooty(game, (50, -50)))
		elif level==2:
			for row in range(1):
				for col in range(10):
					swarm.append(enemies.Normal(game, (50+col*enemies.Enemy.width, row*enemies.Enemy.height)))
		else:
			print("@swarm_generator: I don't know what to give for the number "+str(level))

		#shift swarm to exist just outside of screen
		max_y = 0
		for enemy in swarm:
			if enemy.rect.bottom > max_y: max_y=enemy.rect.bottom
		for enemy in swarm:
			enemy.y-=max_y
		return swarm