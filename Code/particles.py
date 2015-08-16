
# PURPOSE OF THIS GAME:
# To show that we the SHS Game Design Club mean buisness.
# All rights reserved.

import pygame
import random
import main
from pygame.locals import *

"""Holder of the ParticleManager static class, which will handle all particle effects."""

pygame.init()

class ParticleManager:
	"""Handles all of thy particles."""
	effects = []
	@staticmethod
	def update():
		"""Updates all particle effects."""
		for e in ParticleManager.effects: 
			e.update()
			if e.times_up: ParticleManager.effects.remove(e)
	@staticmethod
	def draw(camera):
		"""Draws all particle effects."""
		for e in ParticleManager.effects: e.draw(camera)
	@staticmethod
	def make_explosion(pos, intensity):
		ParticleManager.effects.append(ExplosionEffect(pos, intensity))

class ExplosionEffect:
	explosion_particle_img = pygame.image.load("sprites/explosion_particle.png").convert()
	explosion_particle_img = pygame.transform.scale(explosion_particle_img, (10, 10))
	def __init__(self, pos, intensity):
		self.origin=pos
		self.intensity=intensity
		self.particles=[]
		for x in range(intensity): 
			self.particles.append(ParticleData(pos, random.randint(-intensity, intensity)/5, random.randint(-intensity, intensity)/5, random.randint(5, intensity)))

		self.timer=0
		self.times_up=False #True==effect is done, should be removed
	def update(self):
		for p in self.particles:
			p.x += p.xs
			p.y += p.ys
			#remove particles who's lifespans are over
			if self.timer>=p.lifespan: self.particles.remove(p)

		#self.times_up==True if there are no more particles.
		if len(self.particles)==0: self.times_up=True 

		self.timer+=1 #tick tock.......
	def draw(self, camera):
		for p in self.particles:
			camera.blit_surface(ExplosionEffect.explosion_particle_img, (p.x, p.y))

class ParticleData:
	"""Represents data for a generic particle."""
	def __init__(self, pos, xs, ys, lifespan):
		self.x=pos[0]
		self.y=pos[1]
		self.xs=xs
		self.ys=ys
		self.lifespan=lifespan