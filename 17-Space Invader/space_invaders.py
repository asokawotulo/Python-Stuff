import pygame
from pygame.sprite import Group
from classes.ship import Ship
from classes.bullet import Bullet
from classes.alien import Alien

direction = 1

def createFleet(screen, ship, aliens, screenSize):
	alien = Alien(screen, screenSize)
	alien_height = alien.rect.height
	alien_width = alien.rect.width
	available_space_y = screenSize[1] - (alien_height)
	available_space_x = screenSize[0] - (2 * alien_width)
	number_of_aliens_y = int(available_space_y / (1.5 * alien_height))
	number_of_aliens_x = int(available_space_x / (2 * alien_width))
	for alien_number_x in range(number_of_aliens_x):
		for alien_number_y in range(number_of_aliens_y):
			alien = Alien(screen, screenSize)
			alien.y = alien_height + int(1.5 * alien_height) * alien_number_y
			alien.x = alien_height + int(1.5 * alien_height) * alien_number_x
			alien.rect.y = alien.y
			alien.rect.x = screenSize[0] - alien.x * 1.25
			aliens.add(alien)

def check_fleet_edges(aliens):
	global direction
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(aliens)
			break

def change_fleet_direction(aliens):
	global direction
	for alien in aliens.sprites():
		alien.rect.x -= 10
	direction = direction * -1

def runGame():
	global direction
	# Initialize
	pygame.init()
	gameOver = False

	# Settings
	screen_width = 900
	screen_height = 500
	backgroundColor = (230, 230, 230)

	# Variables
	screen = pygame.display.set_mode((screen_width, screen_height))
	ship = Ship(screen)
	bullets = Group()
	aliens = Group()
	alien = Alien(screen, (screen_width, screen_height))

	createFleet(screen, ship, aliens, (screen_width, screen_height))
	# Looping
	while not gameOver:
		screen.fill(backgroundColor)
		pygame.display.set_caption("Space Invaders")

		# Game controls
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameOver = True
		
		pressed = pygame.key.get_pressed()
		# Keeps ship inside of box
		if pressed[pygame.K_UP] and ship.rect.centery > 0 + int(ship.size[1]/2):
			ship.rect.centery -= 10
		# Keeps ship inside of box
		if pressed[pygame.K_DOWN] and ship.rect.centery < screen_height - int(ship.size[1]/2):
			ship.rect.centery += 10
		if pressed[pygame.K_SPACE] and len(bullets) < 50:
			new_bullet = Bullet(screen, ship)
			bullets.add(new_bullet)
		if pressed[pygame.K_q]: # Quits game on press Q
			gameOver = True

		ship.drawShip()
		collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

		aliens.draw(screen)

		check_fleet_edges(aliens)
		aliens.update(direction)
		bullets.update()

		if pygame.sprite.spritecollideany(ship, aliens):
			print("Ship hit!!!")
		for bullet in bullets.sprites():
			bullet.drawBullet()
		for bullet in bullets.copy():
			if bullet.rect.left >= screen_width:
				bullets.remove(bullet)
		pygame.display.flip()

runGame()