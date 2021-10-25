import sys
import pygame

# =========== Importación de modelos
from models.background import Background
from models.space_ship import SpaceShip
from models.asteroid import Asteroid

# =========== Importación de funciones
from functions.asteroids import generate_asteroids

pygame.init()
pygame.font.init()

# Configuraciones generales
size = width, height = 800, 800
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption('PySpace')

# Generación del texto a poner en la pantalla
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('¡Evita los asteroides!', True, (32, 32, 32), (255, 255, 255))
text_rect = text.get_rect()

# Se instancian los modelos necesarios para el juego
background = Background()
space_ship = SpaceShip()
asteroids = generate_asteroids(8)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if space_ship.get_current_pos()[0] > 0:
            space_ship.move(-1, 0)
    
    if keys[pygame.K_RIGHT]:
        if space_ship.get_current_pos()[0] < width - 150:
            space_ship.move(1, 0)

    if keys[pygame.K_DOWN]:
        if space_ship.get_current_pos()[1] < height - 150:
            space_ship.move(0, 1)
    
    if keys[pygame.K_UP]:
        if space_ship.get_current_pos()[1] > 0:
            space_ship.move(0, -1)
    
    background.update()
    screen.fill(black)

    background.render(screen)
    screen.blit(space_ship.image, space_ship.rect)

    for asteroid in asteroids:
        asteroid.move()
        asteroid.render(screen)
    
    screen.blit(text, (300, 760))

    pygame.display.flip()