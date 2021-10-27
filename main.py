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
space_icon = pygame.image.load('window_icon.png')
pygame.display.set_icon(space_icon)
game_paused = False


# Se genera la imagen para la vida del jugador
hp_image = pygame.image.load('./sprites/space_ship/live.png')
hp_image = pygame.transform.scale(hp_image, (60, 50))

# Generación del texto a poner en la pantalla
# == Texto de información
info_font = pygame.font.Font('freesansbold.ttf', 20)
info_text = info_font.render('¡Evita los asteroides!', True, (32, 32, 32), (255, 255, 255))

# == Texto para mostrar la vida actual del jugador
hp_font = pygame.font.Font('freesansbold.ttf', 16)

# == Texto de pausa del juego
pause_font = pygame.font.Font('freesansbold.ttf', 30)
pause_text = pause_font.render('PAUSA', True, (32, 32, 32), (255, 255, 255))

# Se instancian los modelos necesarios para el juego
background = Background()
space_ship = SpaceShip()
asteroids = generate_asteroids(8)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Se cierra el juego
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                # Tecla para pausar el juego
                game_paused = not game_paused
    
    if game_paused:
        # El juego se encuentra en pausa. Se muestra el mensaje en pantalla
        continue
    
    keys = pygame.key.get_pressed()

    if game_paused:
        background.update()
        screen.fill(black)
        screen.blit(pause_text, (400, 400))
        continue

    if keys[pygame.K_LEFT]:
        if space_ship.get_current_pos()[0] > 0:
            space_ship.move(-1, 0)
    
    if keys[pygame.K_RIGHT]:
        if space_ship.get_current_pos()[0] < width - space_ship.x_scale:
            space_ship.move(1, 0)

    if keys[pygame.K_DOWN]:
        if space_ship.get_current_pos()[1] < height - space_ship.y_scale:
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

        if asteroid.rect.colliderect(space_ship.rect):
            space_ship.check_collision(asteroid)
    
    hp_text = hp_font.render('HP ' + str(space_ship.hp), True, (32, 32, 32), (255, 255, 255))
    
    screen.blit(info_text, (300, 760))
    screen.blit(hp_text, (670, 760))
    screen.blit(hp_image, (615, 740))

    pygame.display.flip()