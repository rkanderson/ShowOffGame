
# PURPOSE OF THIS GAME:
# To show that we the SHS Game Design Club mean buisness.
# All rights reserved.

import pygame
import random

"""All things sound."""

pygame.init()

class MySounds:
	sound_dictionary = {}
	sound_dictionary['explosion1']=pygame.mixer.Sound("sounds/explosion1.wav")
	sound_dictionary['explosion2']=pygame.mixer.Sound("sounds/explosion2.wav")
	sound_dictionary['explosion3']=pygame.mixer.Sound("sounds/explosion3.wav")
	sound_dictionary['explosion4']=pygame.mixer.Sound("sounds/explosion4.wav")
	sound_dictionary['explosion5']=pygame.mixer.Sound("sounds/explosion5.wav")


	@staticmethod
	def start_music():
		#pygame.mixer.music.load("sound/filename.ogg")
		#pygame.mixer.music.play(-1)
		pass
	@staticmethod
	def play_sound(name):
		MySounds.sound_dictionary[name].play()
	@staticmethod
	def play_explosion_sound():
		type = random.randint(1, 5)
		MySounds.sound_dictionary['explosion'+str(type)].play()
