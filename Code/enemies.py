
# PURPOSE OF THIS GAME:
# To show that we the SHS Game Design Club mean buisness.
# All rights reserved.

import pygame
from pygame.locals import *
from random import random
import main

"""This file will contain classes for every different kind of
enemy, each derived from the generic Enemy class."""

pygame.init()

"""
 ______                            
 |  ____|                           
 | |__   _ __   ___ _ __ ___  _   _ 
 |  __| | '_ \ / _ \ '_ ` _ \| | | |
 | |____| | | |  __/ | | | | | |_| |
 |______|_| |_|\___|_| |_| |_|\__, |
                               __/ |
                              |___/ 
"""
class Enemy:
	"""Generic Enemy"""
	width=40
	height=50
	speed=1
	def __init__(self, game, pos, surface=pygame.Surface((40, 50))):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
		self.surface=surface
		self.rect=self.surface.get_rect(x=self.x, y=self.y)
	def update(self, events):
		self.update_position()
		self.y+=self.game.environment_speed
		self.rect.x=self.x
		self.rect.y=self.y
		self.fire_if_necessary()
		self.check_for_player_collision()
		self.remove_if_out_of_bounds()	

	def draw(self, camera):
		camera.blit_surface(self.surface, (self.x, self.y))

	def update_position(self):
		"""Update coordinates and rect's coordinates"""
		self.y+=self.speed

	def fire_if_necessary(self):
		#fire missile.... maybe...
		if random() > 0.998: self.fire()


	def check_for_player_collision(self):
		if pygame.Rect.colliderect(self.rect, self.game.player.rect): #HIT the player!
			self.game.player.is_dead=True #BOOM u dead

	def remove_if_out_of_bounds(self):
		if self.y > main.screen_dimensions[1]: self.game.enemies.remove(self)

	def fire(self):
		"""FIRE ZE MISSILE!"""
		self.game.missiles.append(main.Missile(self.game, (self.x+self.width/2-main.Torpedo.width/2, self.y-20)))

class Normal(Enemy):
	def __init__(self, game, pos):
		surface = pygame.Surface((40, 50))
		surface.fill(main.RED)
		Enemy.__init__(self, game, pos, surface)

class Shooty(Enemy):
	"""Moves slower and shoots more than usual"""
	speed=1
	def __init__(self, game, pos):
		self.surface = pygame.Surface((50, 50))
		self.surface.fill(main.BLUE)
		Enemy.__init__(self, game, pos, self.surface)

	def update_position(self):
		"""Update own coordinates"""
		if not self.y >= 50:
			self.y+=self.speed
		else: self.y -= self.game.environment_speed

	def fire_if_necessary(self):
		#fire missile.... maybe...
		if random() > 0.95: self.fire()

	

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
		
class Usey(Enemy):
	"""Absorbs nearby enemies and fires them towards you, like projectiles."""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass

class Tricksy(Enemy):
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

class Blasty(Enemy):
	"""Shoots beams that bring player closer to enemy border screen"""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass

class Revolty(Enemy):
	"""Every time its hit, it gives a power up to the player."""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass
		
class Meaty(Enemy):
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

class Stitchy(Enemy):
	"""Heals itself overtime if not shot at"""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass

class Barry(Enemy):
	"""Creates a BARRYier in front of the troops. Protects the troops, until BARRY is destroyed."""
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
	def update(self, events):
		pass
	def draw(self, camera):
		pass
