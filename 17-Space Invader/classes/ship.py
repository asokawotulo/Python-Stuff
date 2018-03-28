import pygame
class Ship():
	def __init__(self, screen):
		self.screen = screen
		
		self.image = pygame.image.load("images/ship.png")
		self.image_rotated = pygame.transform.rotate(self.image, -90)
		self.rect = self.image_rotated.get_rect()
		self.size = self.rect.size
		self.screen_rect = screen.get_rect()
		
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left

	def drawShip(self):
		self.screen.blit(self.image_rotated, self.rect)
 