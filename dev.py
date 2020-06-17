#! usr/bin/python3
# dev.py -- side file

import pygame

# Initialize Pygame functions
pygame.init()


# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Colors in the GAME
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


SCREEN_SIZE = 500

# Create the screen
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

""" MAP CLASS """
class MAP:
    def __init__(self):

        self.GRID_NUM = 20
        self.GRID_WIDTH = SCREEN_SIZE/self.GRID_NUM

    def draw(self):
        pass

Map = MAP()
class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(
            screen,
            self.color,
            (self.x*Map.GRID_WIDTH,
            self.y*Map.GRID_WIDTH,
            Map.GRID_WIDTH,
            Map.GRID_WIDTH
            ))
class Snake:
    def __init__(self, segments):
        self.segments=segments

    def draw(self):
        for segment in self.segments:
            segment.draw()

Apple = Block(2, 3, RED)
Player = Snake(segments=[Block(3, 4, BLUE), Block(3, 5, BLUE)])
running = True


while running:
    Apple.draw()
    Player.draw()
    # Iterate over the event list
    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    pygame.display.flip()
