
# PURPOSE OF THIS GAME:
# To show that we the SHS Game Design Club mean buisness.
# All rights reserved.

import pygame
from pygame.locals import *
from enemies import *
from random import random

"""This main file holds the main game loop as well as all
# of the basic classes"""

pygame.init()

# Some color constants
BLUE = (0, 0, 255)
LIGHTER_BLUE = (100, 100, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHTER_RED = (255, 100, 100)



FPS=30
FPSCLOCK=pygame.time.Clock()
screen_dimensions = (500, 700)
DISPLAYSURF = pygame.display.set_mode(screen_dimensions)
pygame.display.set_caption("Showoff")
EVENTS = []

def main():
	"""Starts the game."""
	global game
	game = Game(DISPLAYSURF) # make a new Game object
	running = True
	while running: #<---Start of main game loop. 1 time around = 1 frame 
		EVENTS = pygame.event.get() # update EVENTS

		# See if there's any need to quit (red x button pressed)
		for event in EVENTS:
			if event.type==QUIT:
				running = False

		game.update(EVENTS) # update game state
		game.draw() # draw game

		FPSCLOCK.tick(FPS) # pause a few milliseconds (1/FPS)seconds

class Game:
	"""Top of class hierarchy; the godly class."""
	environment_speed=1
	def __init__(self, screen):
		"""Initializes a new Game object."""
		self.player=Player(self)
		self.enemies=[]
		self.init_enemies()
		self.torpedos=[]
		self.missiles=[]
		self.background=Background(self)
		self.camera=Camera(self, screen, (0,0))
	def update(self, events):
		"""Updates game state."""
		# call all the update methods
		self.player.update(events)
		for enemy in self.enemies:
			enemy.update(events)
		for torpedo in self.torpedos:
			torpedo.update(events)
		for missile in self.missiles:
			missile.update(events)
		self.background.update(events)

		# delete any stray torpedos/missiles (off screen)
		for torpedo in self.torpedos:
			if torpedo.y+Torpedo.height<0: 
				self.torpedos.remove(torpedo)
				#print("Torpedo removed.")
		for missile in self.missiles:
			if missile.y > screen_dimensions[1]:
				self.missiles.remove(missile)
				#print("Missile removed.")

	def draw(self):
		"""Draws itself on camera."""
		# order of draws determines layers
		self.background.draw(self.camera)
		for enemy in self.enemies:
			enemy.draw(self.camera)
		self.player.draw(self.camera)
		for missile in self.missiles:
			missile.draw(self.camera)
		for torpedo in self.torpedos:
			torpedo.draw(self.camera)
		pygame.display.update()

	def init_enemies(self):
		self.enemies.append(Enemy(self, (50, 50)))

class Camera:
	"""Should be utilized by any game object that wishes to draw itself"""
	def __init__(self, game, screen, pos):
		self.game=game
		self.screen=screen
		self.pos=pos
	def blit_surface(self, surface, pos):
		"""Blits a surface onto its own surface at new coordinates based
		off given ones and its own."""
		newx = pos[0] - self.pos[0]
		newy = pos[1] - self.pos[1]
		self.screen.blit(surface, (newx, newy))
	def draw_rect(self, rect, color):
		"""Just like blit_surface but for pygame.Rect."""
		new_rect = pygame.Rect(rect.x-self.pos[0], rect.y-self.pos[1], rect.width, rect.height)
		pygame.draw.rect(self.screen, color, new_rect)

class Player:
	"""What the user controls."""
	def __init__(self, game):
		self.game=game
		self.width=60
		self.height=80
		self.x=screen_dimensions[0]/2-self.width/2
		self.y=600
		self.side_to_side_speed = 5
		self.rect=pygame.Rect(self.x, self.y, self.width, self.height)
		self.move_right=[False, False] # first bool=being treated as pressed by game
		self.move_left = [False, False] # second is being pressed at all ([False, True]="on wait list"
										# this is all done to make controls more comfortable.
	def update(self, events):
		
		# update event-related variables
		for event in events:
			if event.type==KEYDOWN:
				if event.key==K_RIGHT: self.right_pressed()
				elif event.key==K_LEFT: self.left_pressed()
				elif event.key==K_SPACE: self.fire()
			elif event.type==KEYUP:
				if event.key==K_RIGHT: self.right_released()
				elif event.key==K_LEFT: self.left_released()

		# update position
		if self.move_right[0]: self.x += self.side_to_side_speed
		elif self.move_left[0]: self.x -= self.side_to_side_speed
		self.rect.x = self.x
		self.rect.y = self.y



	def draw(self, camera):
		camera.draw_rect(self.rect, BLUE)

	def fire(self):
		"""Fire ze TORPEDO!"""
		self.game.torpedos.append(Torpedo(self.game, (self.x+self.width/2-Torpedo.width/2, self.y-20)))

	def right_pressed(self):
		self.move_right[1]=True
		if not self.move_left[0]: self.move_right[0]=True
	def left_pressed(self):
		self.move_left[1]=True
		if not self.move_right[0]: self.move_left[0]=True
	def right_released(self):
		self.move_right=[False, False]
		if self.move_left[1]: self.move_left[0]=True
	def left_released(self):
		self.move_left=[False, False]
		if self.move_right[1]: self.move_right[0]=True

class Enemy:
	"""Generic Enemy"""
	width=40
	height=50
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
		self.rect=pygame.Rect(self.x, self.y, Enemy.width, Enemy.height)
	def update(self, events):
		#Update coordinates
		self.y+=self.game.environment_speed
		#self.x......

		#update rect
		self.rect.x=self.x
		self.rect.y=self.y

		#fire missile.... maybe...
		if random() > 0.98: self.fire()

	def draw(self, camera):
		camera.draw_rect(self.rect, RED)

	def fire(self):
		"""FIRE ZE MISSILE!"""
		self.game.missiles.append(Missile(self.game, (self.x+self.width/2-Torpedo.width/2, self.y-20)))


class Torpedo:
	"""Those cool things the player fires."""
	height=40
	width=20
	speed=10
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
		self.rect=pygame.Rect(self.x, self.y, Torpedo.width, Torpedo.height)
	def update(self, events):
		#update position
		self.y-=Torpedo.speed
		self.rect.y=self.y

		#check for collision with an enemy
		for enemy in self.game.enemies:
			if pygame.Rect.colliderect(self.rect, enemy.rect): 
				self.game.enemies.remove(enemy)
				self.game.torpedos.remove(self)

	def draw(self, camera):
		camera.draw_rect(self.rect, LIGHTER_BLUE)

class Missile:
	"""Those nasty things Aliens shoot."""
	width=20
	height=40
	speed=10
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
		self.rect=pygame.Rect(self.x, self.y, Missile.width, Missile.height)
	def update(self, events):
		self.y+=Missile.speed
		self.rect.y=self.y
	def draw(self, camera):
		camera.draw_rect(self.rect, LIGHTER_RED)


class Background:
	"""An intense changing Background."""
	def __init__(self, game):
		self.game=game
		self.rect=pygame.Rect(0, 0, screen_dimensions[0], screen_dimensions[1])
	def update(self, events):
		pass
	def draw(self, camera):
		camera.draw_rect(self.rect, BLACK)


# Start game only if this is the module being run.
if __name__=="__main__":
	main()
