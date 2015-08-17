
# PURPOSE OF THIS GAME:
# To show that we the SHS Game Design Club mean buisness.
# All rights reserved.

import pygame
import sound
import particles
from pygame.locals import *
from swarm_generator import SwarmGenerator
from random import random

"""This main file holds the main game loop as well as all
of the basic classes."""

# Note: some ascii art words have been added for easy reading in
# Sublime text. Also for yolo purposes.

pygame.init()

# Some color constants
BLUE = (0, 0, 255)
LIGHTER_BLUE = (100, 100, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHTER_RED = (255, 100, 100)
GREEN = (0, 255, 0)



FPS=30
FPSCLOCK=pygame.time.Clock()
screen_dimensions = (500, 700)
DISPLAYSURF = pygame.display.set_mode(screen_dimensions)
pygame.display.set_caption("Showoff")
EVENTS = []


"""
       _       __                   _        ____  
      | |     / _|                 (_)      / /\ \ 
    __| | ___| |_   _ __ ___   __ _ _ _ __ | |  | |
   / _` |/ _ \  _| | '_ ` _ \ / _` | | '_ \| |  | |
  | (_| |  __/ |   | | | | | | (_| | | | | | |  | |
   \__,_|\___|_|   |_| |_| |_|\__,_|_|_| |_| |  | |
                                            \_\/_/ 
 """                                                                                  
def main():
	"""Starts the game."""
	global game
	game = Game(DISPLAYSURF) # make a new Game object
	running = True
	while running: #<---Start of main game loop. 1 time around = 1 frame

		#Restart the game?
		if game.restart_me: game = Game(DISPLAYSURF)

		EVENTS = pygame.event.get() # update EVENTS

		# See if there's any need to quit (red x button pressed)
		for event in EVENTS:
			if event.type==QUIT:
				running = False

		game.update(EVENTS) # update game state
		game.draw() # draw game

		FPSCLOCK.tick(FPS) # pause a few milliseconds (1/FPS)seconds

"""
   _____                  
  / ____|                     
 | |  __  __ _ _ __ ___   ___ 
 | | |_ |/ _` | '_ ` _ \ / _ \
 | |__| | (_| | | | | | |  __/
  \_____|\__,_|_| |_| |_|\___|
                                                  
"""
class Game:
	"""Top of class hierarchy; the godly class."""
	environment_speed=1
	number_of_waves=3
	time_between_waves=90
	def __init__(self, screen):
		"""Initializes a new Game object."""
		self.player=Player(self)
		self.enemies=[]
		self.swarm_number=0
		self.init_enemies(self.swarm_number)
		self.between_swarm_timer=0 #@main.time_between_waves can call init_enemies again.
		self.torpedos=[]
		self.missiles=[]
		self.background=Background(self)
		self.camera=Camera(self, screen, (0,0))
		self.game_over_img = pygame.image.load("sprites/game_over.png").convert_alpha()
		self.you_win_img = pygame.image.load("sprites/you_win.png").convert_alpha()
		self.game_won=False
		self.restart_me=False # @Game.time_between_waves indicates if the game wants to be restarted (replaced by new one)
	def update(self, events):
		"""Updates game state."""
		for event in events:
			if event.type==KEYDOWN and event.key==K_UP: Game.environment_speed=10
			elif event.type==KEYUP and event.key==K_UP: Game.environment_speed=1
			elif event.type==KEYDOWN and event.key==K_SPACE and (self.player.is_dead or self.game_won):
				self.restart_me=True
		# call all the update methods
		self.camera.update()
		particles.ParticleManager.update()
		if not self.player.exploded: self.player.update(events)
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
 		
 		if len(self.enemies)==0:
 			if self.swarm_number==Game.number_of_waves-1: self.game_won=True
 			elif self.between_swarm_timer==Game.time_between_waves:
 				self.between_swarm_timer=0
 				self.swarm_number+=1
 				self.init_enemies(self.swarm_number)
 			else: self.between_swarm_timer+=1

	def draw(self):
		"""Draws itself on camera."""
		# order of draws determines layers
		self.background.draw(self.camera)
		for enemy in self.enemies:
			enemy.draw(self.camera)
		if not self.player.exploded: self.player.draw(self.camera)
		for missile in self.missiles:
			missile.draw(self.camera)
		for torpedo in self.torpedos:
			torpedo.draw(self.camera)
		particles.ParticleManager.draw(self.camera)
		if self.player.is_dead:
			self.camera.screen.blit(self.game_over_img, (0, 200))
		elif self.game_won:
			self.camera.screen.blit(self.you_win_img, (0, 200))

		pygame.display.update()

	def init_enemies(self, swarm_number):
		self.enemies = SwarmGenerator.generate_swarm(swarm_number, self)
		sound.MySounds.play_sound("swoosh")

"""
  _____                               
  / ____|                              
 | |     __ _ _ __ ___   ___ _ __ __ _ 
 | |    / _` | '_ ` _ \ / _ \ '__/ _` |
 | |___| (_| | | | | | |  __/ | | (_| |
  \_____\__,_|_| |_| |_|\___|_|  \__,_|
                                       
"""
class Camera:
	"""Should be utilized by any game object that wishes to draw itself"""
	def __init__(self, game, screen, pos):
		self.game=game
		self.screen=screen
		self.x=pos[0]
		self.y=pos[1]
		self.shake_offset=[0,0] # x, y
		self.shaking_intensity=0 # starts w/ no shake
	def update(self):
		#print("Camera shake offset=="+str(self.shake_offset[0])+", "+str(self.shake_offset[1]))
		if self.shaking_intensity > 0:
			self.shake(self.shaking_intensity-1)
	def blit_surface(self, surface, pos):
		"""Blits a surface onto its own surface at new coordinates based
		off given ones and its own."""
		newx = pos[0] - self.x + self.shake_offset[0]
		newy = pos[1] - self.y + self.shake_offset[1]
		self.screen.blit(surface, (newx, newy))
	def draw_rect(self, rect, color):
		"""Just like blit_surface but for pygame.Rect."""
		new_rect = pygame.Rect(rect.x-self.x + self.shake_offset[0], rect.y-self.y+self.shake_offset[1], rect.width, rect.height)
		pygame.draw.rect(self.screen, color, new_rect)
	def shake(self, intensity):
		#print ("Camera shake w/ intensity of "+str(intensity))
		self.shaking_intensity=intensity
		self.shake_offset=[intensity, intensity]
		for index in range(2): 
			if random()>0.5: self.shake_offset[index]*=-1

"""
  _____  _                       
 |  __ \| |                      
 | |__) | | __ _ _   _  ___ _ __ 
 |  ___/| |/ _` | | | |/ _ \ '__|
 | |    | | (_| | |_| |  __/ |   
 |_|    |_|\__,_|\__, |\___|_|   
                  __/ |          
                 |___/         
"""
class Player:
	"""What the user controls."""
	time_between_shots=10
	def __init__(self, game):
		self.game=game
		self.width=50
		self.height=40
		self.x=screen_dimensions[0]/2-self.width/2
		self.y=600
		self.side_to_side_speed = 7
		self.shot_timer=Player.time_between_shots #@10==can shoot
		self.rect=pygame.Rect(self.x, self.y, self.width, self.height)
		self.is_dead=False
		self.exploded=False
		self.move_right=[False, False] # first bool=being treated as pressed by game
		self.move_left = [False, False] # second is being pressed at all ([False, True]="on wait list"
										# this is all done to make controls more comfortable.
		self.space_pressed=False
	def update(self, events):
		
		# update event-related variables
		for event in events:
			if event.type==KEYDOWN:
				if event.key==K_RIGHT: self.right_pressed()
				elif event.key==K_LEFT: self.left_pressed()
				elif event.key==K_SPACE: self.space_pressed=True
			elif event.type==KEYUP:
				if event.key==K_RIGHT: self.right_released()
				elif event.key==K_LEFT: self.left_released()
				elif event.key==K_SPACE: self.space_pressed=False

		# update position
		if self.move_right[0]: self.x += self.side_to_side_speed
		elif self.move_left[0]: self.x -= self.side_to_side_speed
		if self.x < 0: self.x=0
		elif self.x + self.width > screen_dimensions[0]: self.x = screen_dimensions[0]-self.width
		self.rect.x = self.x
		self.rect.y = self.y

		if self.space_pressed and self.shot_timer>=Player.time_between_shots:
			self.fire()
			self.shot_timer=0

		#update shot timer
		if self.shot_timer<Player.time_between_shots: self.shot_timer+=1

		#if dead, explode
		if self.is_dead: self.explode()

	def draw(self, camera):
		camera.draw_rect(self.rect, BLUE)

	def explode(self):
		#spawn explosion at coordinates?
		sound.MySounds.play_sound("player_explosion")
		self.exploded=True
		particles.ParticleManager.make_explosion((self.rect.centerx, self.rect.centery), 50)
		self.game.camera.shake(20)

	def fire(self):
		"""Fire ze TORPEDO!"""
		self.game.torpedos.append(Torpedo(self.game, (self.x+self.width/2-Torpedo.width/2, self.y-5)))
		sound.MySounds.play_sound('shoot')

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


"""
 _______                        _       
 |__   __|                      | |      
    | | ___  _ __ _ __   ___  __| | ___  
    | |/ _ \| '__| '_ \ / _ \/ _` |/ _ \ 
    | | (_) | |  | |_) |  __/ (_| | (_) |
    |_|\___/|_|  | .__/ \___|\__,_|\___/ 
                 | |                     
                 |_|                    
"""
class Torpedo:
	"""Those cool things the player fires."""
	height=20
	width=10
	speed=10
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
		self.rect=pygame.Rect(self.x, self.y, Torpedo.width, Torpedo.height)
		self.gone=False
	def update(self, events):
		#update position
		self.y-=Torpedo.speed-self.game.environment_speed
		self.rect.y=self.y

		#check for collision with an enemy
		for enemy in self.game.enemies:
			if pygame.Rect.colliderect(self.rect, enemy.rect): # IT'S A HIT!
				self.game.enemies.remove(enemy)
				self.game.torpedos.remove(self)
				self.game.camera.shake(5)
				sound.MySounds.play_explosion_sound()
				particles.ParticleManager.make_explosion((enemy.rect.centerx, enemy.rect.centery), 20)
				self.gone=True

		#check for collision with a missile
		if not self.gone:
			for missile in self.game.missiles:
				if pygame.Rect.colliderect(self.rect, missile.rect): # IT'S A HIT!
					self.game.missiles.remove(missile)
					self.game.torpedos.remove(self)
					self.game.camera.shake(2)
					sound.MySounds.play_explosion_sound()
					particles.ParticleManager.make_explosion((self.rect.centerx, self.rect.centery), 10)

	def draw(self, camera):
		camera.draw_rect(self.rect, LIGHTER_BLUE)

"""
 __  __ _         _ _      
 |  \/  (_)       (_) |     
 | \  / |_ ___ ___ _| | ___ 
 | |\/| | / __/ __| | |/ _ \
 | |  | | \__ \__ \ | |  __/
 |_|  |_|_|___/___/_|_|\___|

"""
class Missile:
	"""Those nasty things Aliens shoot."""
	width=10
	height=20
	speed=7
	def __init__(self, game, pos):
		self.game=game
		self.x=pos[0]
		self.y=pos[1]
		self.rect=pygame.Rect(self.x, self.y, Missile.width, Missile.height)
	def update(self, events):
		self.y+=Missile.speed+self.game.environment_speed
		self.rect.y=self.y
		if pygame.Rect.colliderect(self.rect, self.game.player.rect): #HIT the player!
			self.game.player.is_dead=True #BOOM u dead
			self.game.missiles.remove(self)
	def draw(self, camera):
		camera.draw_rect(self.rect, LIGHTER_RED)

"""
 ____             _                                   _ 
 |  _ \           | |                                 | |
 | |_) | __ _  ___| | ____ _ _ __ ___  _   _ _ __   __| |
 |  _ < / _` |/ __| |/ / _` | '__/ _ \| | | | '_ \ / _` |
 | |_) | (_| | (__|   < (_| | | | (_) | |_| | | | | (_| |
 |____/ \__,_|\___|_|\_\__, |_|  \___/ \__,_|_| |_|\__,_|
                        __/ |                            
                       |___/                             
"""
class Background:
	"""An intense changing Background."""
	star_speed = 1
	def __init__(self, game):
		self.game=game
		self.rect=pygame.Rect(0, 0, screen_dimensions[0], screen_dimensions[1])
		self.stars=[] #array of pygame.Rects
	def update(self, events):
		#create new star?
		if random() > 0.75:
			#print ("star created")
			starx=random()*screen_dimensions[0]
			self.stars.append(pygame.Rect(starx, 0, 2, 2))
		#update star positions/ remove out of bounds ones
		for star in self.stars:
			star.y+=Background.star_speed*Game.environment_speed
			if star.y > screen_dimensions[1]: self.stars.remove(star)

	def draw(self, camera):
		self.game.camera.screen.fill(BLACK)
		for star in self.stars:
			camera.draw_rect(star, WHITE)


# Start game only if this is the module being run.
if __name__=="__main__":
	main()
