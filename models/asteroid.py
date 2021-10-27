import random
import pygame

class Asteroid():
    '''
        Esta clase representa a los asteroides
        que aparecen en la pantalla
    '''
    images_paths = ['./sprites/asteroids/asteroid1.png', './sprites/asteroids/asteroid2.png'] # Rutas de sprites de los asteroides
    damages = [2.5, 4.5] # Posibles daños 
    velocities = [0.3, 0.35] # Posibles velocidades
    movement_types = [1, 2, 3, 4]

    def __init__(self, type=None):
        '''
            Genera un nuevo asteroide según el tipo entregado (si existe)

            Args:
                type (int): Tipo de asteroide. Aleatorio por defecto.
        '''
        self.generate(type)
    
    def generate(self, type=None):
        self.type = type if type is not None else random.randint(0, 1)
        self.image = pygame.image.load(self.images_paths[self.type])
        self.image = pygame.transform.scale(self.image, (80, 80))

        self.damage = self.damages[self.type]
        self.velocity = self.velocities[self.type]
        self.x_movement = bool(random.randint(0, 1))
        self.x_movement_sign = random.choice([1, -1])
        self.x_movement_count = 0

        self.movement_type = random.choice(self.movement_types)

        if self.movement_type == 1:
            self.x_max_movement = 800
        
        if self.movement_type == 2:
            self.x_max_movement = 900
        
        if self.movement_type == 3:
            self.x_max_movement = 1200
        
        if self.movement_type == 4:
            self.x_max_movement = 1500

        # Posiciones iniciales del asteroide
        self.x = random.randint(0, 700)
        self.y = random.randint(-300, 0)
    
    def move(self):
        '''
            Actualización de coordenadas del fondo 
            según la velocidad de movimiento establecida
        ''' 

        if self.x >= 800 or self.y >= 800:
            self.generate()

        if self.x_movement:
            if self.x_movement_count == self.x_max_movement:
                self.x_movement_sign *= -1
                self.x_movement_count = 0

                if self.type == 1:
                    # Se agrega dificultad seleccionando un nuevo máximo
                    # de movimiento en el eje x para cambiar el sentido
                    self.x_max_movement = random.randint(1500, 2000)

        
            self.x += (self.velocity * self.x_movement_sign)
            self.x_movement_count += 1

        self.y += self.velocity

    
    def rotate(self):
        '''
            Permite realizar rotaciones del rectángulo
        '''
    
    def render(self, display):
        '''
            Renderiza la posición del asteroide 

            Args:
                display (object): Objeto que representa al display de PyGame
        '''
        self.rect = display.blit(self.image, (self.x, self.y))
    
    

    
