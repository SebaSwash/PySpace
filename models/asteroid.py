import random
import pygame

class Asteroid():
    '''
        Esta clase representa a los asteroides
        que aparecen en la pantalla
    '''
    images_paths = ['./sprites/asteroids/asteroid1.png', './sprites/asteroids/asteroid2.png']
    damages = [15, 30]


    def __init__(self, type=None):
        '''
            Genera un nuevo asteroide según el tipo entregado (si existe)

            Args:
                type (int): Tipo de asteroide. Aleatorio por defecto.
        '''
        self.type = type if type is not None else random.randint(0, 1)
        self.image = pygame.image.load(self.images_paths[self.type])


        # Se obtiene el rectángulo en base a la imagen generada
        self.rect = self.image.get_rect()

    def set_initial_position(self, screen_width):
        '''
            Método para situar el asteroide en una posición inicial
            aleatoria en el eje x

            Args:  
                screen_width (int): Largo de la ventana
        '''

        self.rect.x = random.randint(0, screen_width)
        self.rect.y = 0
    
    

    
