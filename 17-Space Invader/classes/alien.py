import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self, screen, screenSize):
		super(Alien, self).__init__()

		self.screen = screen
		self.screenSize = screenSize

		self.image = pygame.image.load("images/alien.bmp")
		self.image_rotated = pygame.transform.rotate(self.image, 90)
		self.rect = self.image_rotated.get_rect()
		self.rect.x = screenSize[0] - self.rect.size[0] * 2
		self.rect.y = screenSize[1] - self.rect.size[1] * 2
		self.screen_rect = screen.get_rect()

	def drawAlien(self):
		self.screen.blit(self.image_rotated, self.rect)

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >= screen_rect.bottom:
			return True
		elif self.rect.top <= 0:
			return True

	def update(self, direction):
		self.y -= 1 * direction
		self.rect.y = self.y