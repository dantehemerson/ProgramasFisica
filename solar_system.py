import pygame
import sys
import math
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sistema Solar")

FPS = 30 # Frames por segundo
fpsClock = pygame.time.Clock()

# Colores
RED  = (255, 0,   0)
BLUE = (  0, 0, 255)
BLACK = (0, 0,0)
EARTH_COLOR = (8, 141, 249)
SUN_COLOR = (255, 241, 12)
MERCURY_COLOR = (97, 86, 74)
JUPITER_COLOR = (124, 124, 124)
VENUS_COLOR = (253, 95, 34)
MARS_COLOR =(168, 40, 1)
URANUS_COLOR = (181, 212, 230)
SATURN_COLOR =(185, 194, 113)

DataPlanet = {
    # Planet   radius |  color | velocity
    "Sun"   : (40,     SUN_COLOR, 1),
    "Mercury": (8,     MERCURY_COLOR, 3),
    "Earth" : (12,     EARTH_COLOR, 2),
    "Jupiter": (20,  JUPITER_COLOR, 1),
    "Venus" : (14,  VENUS_COLOR, 1),
    "Uranus" : (60, URANUS_COLOR, 1),
    "Saturn" : (50, SATURN_COLOR, 1),
    "Mars" : (20, MARS_COLOR, 1)

}



class Circle:
    def __init__(self, center_x, center_y, radius, color):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.backgroundColor = color

    def draw(self):
        pygame.draw.circle(DISPLAY, self.backgroundColor, (int(self.center_x), int(self.center_y)), self.radius, 0)

    def setCenter(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y

    def getCenterX(self):
        return self.center_x

    def getCenterY(self):
        return self.center_y

class Planet(Circle):
    def __init__(self, c_x, c_y, planetName, radiusRotation):
        Circle.__init__(self, 0, 0, DataPlanet[planetName][0], DataPlanet[planetName][1])
        self.radiusRotation = radiusRotation
        self.planetName = planetName    
        self.c_x = c_x
        self.c_y = c_y

        self.angle = 0  # El angulo inicial será 0°
        # Configurando la posición del planeta
        self.x = math.cos(math.radians(self.angle))
        self.y = math.sin(math.radians(self.angle))
        self.x *= radiusRotation
        self.y *= radiusRotation

        self.setCenter(self.c_x + self.x, self.c_y + self.y)

    def update(self):
        self.angle += DataPlanet[self.planetName][2]
        if self.angle > 360:
            self.angle = 1
         # Configurando la posición del planeta
        self.x = math.cos(math.radians(self.angle))
        self.y = math.sin(math.radians(self.angle))
        self.x *= self.radiusRotation
        self.y *= self.radiusRotation

        self.setCenter(self.c_x + self.x, self.c_y + self.y)




def main():
    sun = Planet(400, 300, 'Sun', 0)
    mercury = Planet(400, 300, 'Mercury', 70)
    earth = Planet(400, 300, 'Earth', 150)
    jupiter = Planet(400, 300, 'Jupiter', 200)
    mars = Planet(400, 300, 'Mars', 100)
    saturn = Planet(400, 300, 'Saturn', 100)
    venus = Planet(400, 300, 'Venus', 108)

    while True:
        DISPLAY.fill(BLACK)
        # Capturando los eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #Actualizando
        sun.update()

        earth.setCenter(sun.getCenterX(), sun.getCenterY())
        earth.update()
        mercury.setCenter(sun.getCenterX(), sun.getCenterY())
        mercury.update()
        jupiter.setCenter(sun.getCenterX(), sun.getCenterY())
        jupiter.update()
        mars.setCenter(sun.getCenterX(), sun.getCenterY())
        mars.update()
        saturn.setCenter(sun.getCenterX(), sun.getCenterY())
        saturn.update()
        venus.setCenter(sun.getCenterX(), sun.getCenterY())
        venus.update()

        # Dibujando
        sun.draw()
        mercury.draw()
        venus.draw()
        earth.draw()
        jupiter.draw()


        pygame.display.update()
        fpsClock.tick(FPS)

main()
