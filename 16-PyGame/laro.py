import pygame
def subok():
	pygame.init()
	screenWidth = 400
	screenHeight = 300
	screen = pygame.display.set_mode((screenWidth, screenHeight))
	done = False
	is_blue = True
	boxWidth = 60
	boxHeight = 60
	x = 30
	y = 30

	clock = pygame.time.Clock()

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				is_blue = not is_blue

		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_UP] and y > 0:
			y -= 3
		if pressed[pygame.K_DOWN] and y < screenHeight - boxHeight:
			y += 3
		if pressed[pygame.K_LEFT] and x > 0:
			x -= 3
		if pressed[pygame.K_RIGHT] and x < screenWidth - boxWidth:
			x += 3

		screen.fill((0, 0, 0))
		if is_blue: color = (0, 128, 255)
		else: color = (255, 100, 0)
		pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

		pygame.display.flip()
		clock.tick(60)
subok()