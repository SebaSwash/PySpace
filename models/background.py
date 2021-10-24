import pygame

class Background():
    '''
        Esta clase representa al fondo del juego.
    '''
    image_path = './sprites/environment/background.png'

    def __init__(self):
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()

        self.y1 = 0
        self.x1 = 0

        self.y2 = -self.rect.height
        self.x2 = 0

        self.moving_speed = 0.2

    def update(self):
        '''
            Actualización de coordenadas del fondo 
            según la velocidad de movimiento establecida
        '''
        self.y1 += self.moving_speed
        self.y2 += self.moving_speed

        if self.y1 > self.rect.height:
            self.y1 = -self.rect.height
        
        if self.y2 > self.rect.height:
            self.y2 = -self.rect.height
    
    def render(self, display):
        '''
            Renderiza la posición del fondo 

            Args:
                display (object): Objeto que representa al display de PyGame
        '''
        display.blit(self.image, (self.x1, self.y1))
        display.blit(self.image, (self.x2, self.y2))
        
