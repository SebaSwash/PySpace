import os
import pygame

class SpaceShip():
    '''
        Esta clase representa la nave espacial o naves espaciales
        que se agregan a la ventana del juego.

        Parámetros
        ----------
        speed : int
            Indica la magnitud de velocidad con la que se va a mover un objeto en la pantalla
            (ponderación con las coordenadas)
    '''

    image_path = './sprites/space_ship/ship1.png'

    def __init__(self, speed=None):
        # Se genera el objeto y el rectángulo mediante la librería de PyGame
        # para utilizarlo en el juego

        self.image = pygame.image.load(self.image_path)

        self.x_scale = 70
        self.y_scale = 140
        self.hp = 100 # HP (vida) inicial

        self.image = pygame.transform.scale(self.image, (70, 140))

        # Se ajusta la velocidad de movimiento del rectángulo
        self.speed = speed if speed is not None else 1

        # Se obtiene el rectángulo en base a la imagen generada
        self.rect = self.image.get_rect()
        self.set_position(300, 600)
        self.colliding = False # Permite determinar cuando se termina de colisionar con un objeto
    
    def set_position(self, x, y):
        '''
            Método que permite modificar la posición del rectángulo de la nave
            según las coordenadas indicadas.

            Args:
                x (int): Nueva posición en el eje x (horizontal)
                y (int): Nueva posición en el eje y (vertical)
        '''

        self.rect.x = x
        self.rect.y = y

    def move(self, x ,y):
        '''
            Método que permite desplazar la posición actual del rectángulo de la nave
            en (x, y) unidades

            Args:
                x (int): Cantidad de aumento en el eje x (horizontal)
                y (int): Cantidad de aumento en el eje y (vertical)
        '''

        self.rect.x += (x * self.speed)
        self.rect.y += (y * self.speed)
    
    def get_current_pos(self):
        '''
            Método que permite obtener la posición actual del rectángulo de la nave

            Returns:
                (x, y): Tupla que contiene la posición x (horizontal) e y (vertical)
        '''

        return (self.rect.x, self.rect.y)
    

    def check_collision(self, asteroid):
        '''
            Método que permite analizar con mayor precisión si existe una colisión entre un asteroide
            y la nave del usuario

            Args:
                asteroid (object): Objeto que representa al asteroide involucrado en la colisión
        '''

        if abs(self.rect.x - asteroid.rect.x) <= 1 or abs(self.rect.y - asteroid.rect.y) <= 1:
            if self.colliding:
                return

            # Colisión
            self.colliding = True 
            self.hp -= asteroid.damage # Actualización de HP según el daño del asteroide (tipo)

            if self.hp <= 0:
                # Game Over
                self.hp = 0
            
            # Se inicia el efecto de sonido del impacto
            pygame.mixer.pre_init()
            pygame.mixer.init()

            pygame.mixer.music.load(os.path.normpath(os.path.join(os.getcwd(), 'sounds/hit.mp3')))
            pygame.mixer.music.play()

        else:
            self.colliding = False
        