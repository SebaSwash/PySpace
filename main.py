import sys
import pygame

# =========== Importación de modelos
from models.background import Background
from models.space_ship import SpaceShip

# =========== Importación de funciones
from functions.asteroids import generate_asteroids

pygame.init()

# Configuraciones generales
size = width, height = 800, 800
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)

# Se instancian los modelos necesarios para el juego
background = Background()
space_ship = SpaceShip()

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
    
    background.update()
    screen.fill(black)

    background.render(screen)

    screen.blit(space_ship.image, space_ship.rect)

    pygame.display.flip()