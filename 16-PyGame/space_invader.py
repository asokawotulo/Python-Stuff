import pygame

def runGame():
	# Initialize Game
	pygame.init()

	# Screen Settings
	screenWidth = 500
	screenHeight = 400
	screen = pygame.display.set_mode((screenWidth, screenHeight))

	# Default Settings
	gameOver = False
	backgroundColor = (26, 26, 26)
	pygame.display.set_caption("Space Invaders")

	while True:
		screen.fill(backgroundColor)