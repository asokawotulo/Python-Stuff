import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
	def __init__(self, screen, ship):
		super(Bullet, self).__init__()
		self.screen = screen

		self.bulletSpeed = 5
		self.bulletHeight = 5
		self.bulletWidth = 15
		self.bulletColor = (60, 60, 60)

		self.rect = pygame.Rect(0, 0, self.bulletWidth, self.bulletHeight)
		self.rect.centery = ship.rect.centery
		self.rect.right = ship.rect.right

		self.x = float(self.rect.x)

	def update(self):
		self.x += self.bulletSpeed
		self.rect.x = self.x

	def drawBullet(self):
		pygame.draw.rect(self.screen, self.bulletColor, self.rect)