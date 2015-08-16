
# PURPOSE OF THIS GAME:
# To show that we the SHS Game Design Club mean buisness.
# All rights reserved.

import pygame
import main
from pygame.locals import *
from random import random

"""This file will contain classes for every different kind of
enemy, each derived from the generic Enemy class."""

pygame.init()

class Shooty(main.Enemy):
	"""Moves slower and shoots more than usual"""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass

class Cloaky(main.Enemy):
	"""Becomes almost invisible, then uncloacks in front of your face."""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass

class Lazy(main.Enemy):
	"""Stays in one place and shoots big lasers."""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass
		
class Zoomy(main.Enemy):
	"""Faster than normal and goes in little squiggly motions."""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass
		
class Usey(main.Enemy):
	"""Absorbs nearby enemies and fires them towards you, like projectiles."""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass

class Tricksy(main.Enemy):
	"""Tricks the player by fake firing shots, then firing a large shot that the player has to 
	move to the far edge of the screen to avoid."""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass
class Blasty(main.Enemy):
	"""Shoots beams that bring player closer to enemy border screen"""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass
class Revolty(main.Enemy):
	"""Every time its hit, it gives a power up to the player."""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass
class Meaty(main.Enemy):
	"""Spawns new Shootys around it, and uses them like a meat shield. Destroying all of the shootys gives you a 
	10 second time gap to fire at it and destroy it. 
	After that, it regenerates the shootys. Can do this a max of 3 times."""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass
class Stitchy(main.Enemy):
	"""Heals itself overtime if not shot at"""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass
class Shooty(main.Enemy):
	"""Moves slower and shoots more than usual"""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass
class Barry(main.Enemy):
	"""Creates a BARRYier in front of the troops. Protects the troops, until BARRY is destroyed."""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass
