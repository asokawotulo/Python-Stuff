import pygame
def subok():
	pygame.init()
	screen = pygame.display.set_mode((400, 300))
	done = False
	is_blue = True
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
		if pressed[pygame.K_UP]:
			y -= 3
			if y < -59:
				y = 299
		if pressed[pygame.K_DOWN]:
			y += 3
			if y > 301:
				y = -59
		if pressed[pygame.K_LEFT]:
			x -= 3
			if x < -59:
				x = 399
		if pressed[pygame.K_RIGHT]:
			x += 3
			if x > 401:
				x = -59

		screen.fill((0, 0, 0))
		if is_blue: color = (0, 128, 255)
		else: color = (128, 100, 0)
		pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

		pygame.display.flip()
		clock.tick(120)
subok()