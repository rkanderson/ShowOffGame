
# PURPOSE OF THIS GAME:
# To show that we the SHS Game Design Club mean buisness.
# All rights reserved.

import pygame
from pygame.locals import *
from aliens import *

# This main class holds the main game loop as well as all
# of the basic classes.

pygame.init()

FPS=30
FPSCLOCK=pygame.time.Clock()
screen_dimensions = (500, 700)
DISPLAYSURF = pygame.display.set_mode(screen_dimensions)
pygame.display.set_caption("Showoff")
EVENTS = []

def main():
	"""Starts the game."""
	global game
	game = Game() # make a new Game object
	running = True
	while running: #<---Start of main game loop. 1 time around = 1 frame 
		EVENTS = pygame.event.get() # update EVENTS

		# See if there's any need to quit (red x button pressed)
		for event in EVENTS:
			if event.type==QUIT:
				running = False

		game.update(EVENTS) # update game state
		game.draw(DISPLAYSURF) # draw game

		FPSCLOCK.tick(FPS) # pause a few milliseconds (1/FPS)seconds

class Game:
	"""Top of class hierarchy; the godly class."""
	def __init__(self):
		"""Initializes a new Game object."""
		pass
	def update(self, events):
		"""Updates game state."""
		pass
	def draw(self, screen):
		"""Draws itself on given screen."""
		pass

class Player:
	"""What the user controls."""
	def __init__(self, game):
		self.game=game
	def update(self, events):
		pass
	def draw(self, screen):
		pass

class Alien:
	"""Those bad things that you gotta shoot at."""
	def __init__(self, game):
		self.game=game
	def update(self, events):
		pass
	def draw(self, screen):
		pass

class Torpedo:
	"""Those cool things the player fires."""
	def __init__(self, game):
		self.game=game
	def update(self, events):
		pass
	def draw(self, screen):
		pass

class Missile:
	"""Those nasty things Aliens shoot."""
	def __init__(self, game):
		self.game=game
	def update(self, events):
		pass
	def draw(self, screen):
		pass


class Background:
	"""An intense changing Background."""
	def __init__(self, game):
		self.game=game
	def update(self, events):
		pass
	def draw(self, screen):
		pass


# Start game only if this is the module being run.
if __name__=="__main__":
	main()
