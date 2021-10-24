import random

from pathlib import Path
import sys
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from models import asteroid

def generate_asteroids(amount, type=None):
    '''
        Función que permite obtener una lista de asteroides (objetos)

        Args:
            amount (int): Cantidad de asteroides a generar
            type (int): Tipo de asteroide a generar. Aleatorio por defecto.

        Returns: Una lista que contiene los objetos generados
    '''
    asteroids = []
    random_type = True if type is None else False

    for i in range(amount):

        if random_type:
            type = random.randint(0, 1)

        asteroids.append(asteroid.Asteroid(type))
        print(asteroids[i].type)
    

    return asteroids