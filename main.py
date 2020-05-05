#! usr/bin/python3
# main.py -- main file
# Import Pygame
import pygame, time

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

# setup our screen to draw on
# Define Constant for the size of our screen
SCREEN_SIZE = 500

# Create the screen
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

# Number of blocks that span a length
GRID_NUM = 20
GRID_WIDTH = SCREEN_SIZE/GRID_NUM

# Colors in the GAME
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Run until game ends
running = True

class Block:
    color = GREEN
    def __init__(self, gridX, gridY):
        self.x = gridX
        self.y = gridY


    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x*GRID_WIDTH, self.y*GRID_WIDTH, GRID_WIDTH, GRID_WIDTH))


class Snake:

    def __init__(self, segments):
        self.segments = segments

        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.direction = 'DOWN'

    def draw(self):
        for segment in self.segments:
            segment.draw()
            #print(segment.x, segment.y)

    def move(self):
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        print(self.segments[0].x)
        newBlock = [0,0]
        if self.direction == 'RIGHT':
            newBlock[0] = self.head.x+1
            newBlock[1] = self.head.y
        if self.direction == 'UP':
            newBlock[0] = self.head.x
            newBlock[1] = self.head.y-1
        if self.direction == 'DOWN':
            newBlock[0] = self.head.x
            newBlock[1] = self.head.y+1
        if self.direction == 'LEFT':
            newBlock[0] = self.head.x-1
            newBlock[1] = self.head.y
        self.head = Block(newBlock[0], newBlock[1])
        self.segments.append(self.head)

        #self.segments.pop(-1)
        """
        self.head = self.segments[0]

        if self.direction == 'RIGHT':
            nextHead = Block(self.head.x+1, self.head.y)

        elif self.direction == 'DOWN':
            nextHead = Block(self.head.x, self.head.y+1)

        elif self.direction == 'LEFT':
            nextHead = Block(self.head.x-1, self.head.y)

        elif self.direction == 'UP':
            nextHead = Block(self.head.x, self.head.y-1)

        self.segments.append(nextHead) # Add our new head
        self.segments.pop(-1) # Delete the tail(the last element in the array)
        """
    def update(self, keyPressed):
        if keyPressed==K_LEFT:
            self.direction = 'LEFT'
            print('Moving Left!')
        elif keyPressed == K_UP:
            self.direction = 'UP'
            print('Moving Up!')
        elif keyPressed == K_DOWN:
            self.direction = 'DOWN'
            print('Moving Down!')
        elif keyPressed == K_RIGHT:
            self.direction = 'RIGHT'
            print('Moving Right!')

snake = Snake(segments=[Block(5, 4), Block(5, 3), Block(5, 2), Block(4, 2), Block(3, 2)])
clock = pygame.time.Clock()
clock.tick(10)
# === GAME LOOP === #
while running:

    # The Game Loop does the following things
    # 1. Event Handler (handle user's clicks!)
    # 2. Draw surfaces onto SCREEN
    # 3. [Re]Draw SCREEN

    # Event Handler
    # Check every event in the event list
    for event in pygame.event.get():
        # If the user presses a key...
        if event.type == KEYDOWN:
            #... Was that key the Escape Key?
            if event.key == K_ESCAPE:
                # IF it was, then quit the game
                running = False
            snake.update(keyPressed=event.key)
            print(event.key)

        elif event.type == QUIT:
            running = False


    # Fill the Background with BLACK
    screen.fill(BLACK)
    snake.draw()
    snake.move()
    #V.sleep(1)
    #snake.move()
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
