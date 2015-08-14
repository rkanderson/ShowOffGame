
# PURPOSE OF THIS GAME:
# To show that we the SHS Game Design Club mean buisness.
# All rights reserved.

import pygame
from pygame.locals import *
from random import random
from main import *

"""This file will contain classes for every different kind of
enemy, each derived from the generic Enemy class."""

pygame.init()

class Shooty(Enemy):
	"""Moves slower and shoots more than usual"""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass

class Cloaky(Enemy):
	"""Becomes almost invisible, then uncloacks in front of your face."""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass

class Lazy(Enemy):
	"""Stays in one place and shoots big lasers."""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass
		
class Zoomy(Enemy):
	"""Faster than normal and goes in little squiggly motions."""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass
		
