#! usr/bin/python3
# main.py -- main file
# Import Pygame
import pygame
import time
import random

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
SCORE = 0

def showScore(SCORE):

    font = pygame.font.Font('freesansbold.ttf', 20)
    # create a text suface object,
    # on which text is drawn on it.
    text = font.render("SCORE:" + str(SCORE), True, WHITE)

    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (SCREEN_SIZE-60, SCREEN_SIZE-10)

    screen.blit(text, textRect)

# Number of locks that span a length
GRID_NUM = 15
GRID_WIDTH = SCREEN_SIZE/GRID_NUM
LINE_WIDTH = 0
SNAKE_SPEED = 6

# Colors in the GAME
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


""" Note: x is not the actual location, but the GRID
location. """

# Draw the Grid for the map
def drawMap(screen):
    screen.fill(BLACK)
    for x in range(GRID_NUM):
        pygame.draw.line(screen, WHITE, (x*GRID_WIDTH, 0), (x*GRID_WIDTH, GRID_WIDTH*GRID_NUM),\
        LINE_WIDTH)
    for y in range(GRID_NUM):
        pygame.draw.line(screen, WHITE, (0, y*GRID_WIDTH), (GRID_WIDTH*GRID_NUM, y*GRID_WIDTH),\
        LINE_WIDTH)








class Block:
    color=GREEN
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x*GRID_WIDTH, self.y*GRID_WIDTH, GRID_WIDTH, GRID_WIDTH))

    def checkCollision(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
# TODO: Make Apple class a subClass of Block,
# so we can inherit the functions from block

# Fold this up
class Apple:
    color = RED
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def spawn(self, snake):
        self.x = random.randint(0, GRID_NUM-1)
        self.y = random.randint(0, GRID_NUM-1)
        for segment in snake.segments:
            if self.x == segment.x and self.y == segment.y:
                self.x = random.randint(0, GRID_NUM-1)
                self.y = random.randint(0, GRID_NUM-1)
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x*GRID_WIDTH, self.y*GRID_WIDTH, GRID_WIDTH, GRID_WIDTH))

    def checkCollision(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
class Snake:

    def __init__(self, segments):
        self.segments = segments

        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.direction = 'UP'
        self.nextDirection = self.direction

    def draw(self):
        for segment in self.segments:
            segment.draw()
            print(segment.x, segment.y)
            print("My Stupid Head: ", self.head.x, self.head.y)
            #print(segment.x, segment.y)

    def move(self, apple):
        self.checkMove()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
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
        newBlock = Block(newBlock[0], newBlock[1])
        self.segments.insert(0, newBlock)
        self.head = self.segments[0]
        if self.checkAppleCollision(apple):
            pass
        else:
            self.segments.pop(-1)
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
    def collision(self):
        if self.checkWallCollision() or self.checkSelfCollision():
            return True
        else: pass
    def checkWallCollision(self):
        if self.head.x > (GRID_NUM-1) or self.head.x < 0 or\
         self.head.y < 0 or self.head.y > (GRID_NUM-1):
         return True

    def checkSelfCollision(self):
        for segment in self.segments[1:]:
            if self.head.checkCollision(segment):
                print("collided with segment: " + str(self.segments.index(segment)))
                return True
            else: pass
    def update(self, keyPressed):
        if keyPressed==K_LEFT:
            self.nextDirection = 'LEFT'
            print('Moving Left!')
        elif keyPressed == K_UP:
            self.nextDirection = 'UP'
            print('Moving Up!')
        elif keyPressed == K_DOWN:
            self.nextDirection = 'DOWN'
            print('Moving Down!')
        elif keyPressed == K_RIGHT:
            self.nextDirection = 'RIGHT'
            print('Moving Right!')
    def checkAppleCollision(self, apple):
        collision = self.head.checkCollision(apple)
        return collision

    def checkMove(self):
        if self.direction=='RIGHT' and self.nextDirection=='LEFT':
            pass
        elif self.direction=='DOWN' and self.nextDirection=='UP':
            pass
        elif self.direction=='UP' and self.nextDirection=='DOWN':
            pass
        elif self.direction=='LEFT' and self.nextDirection=='RIGHT':
            pass
        else:
            self.direction = self.nextDirection

snake = Snake(segments=[Block(5, 4), Block(5, 3)])
clock = pygame.time.Clock()

apple = Apple(0, 0)
apple.spawn(snake)


# Run until game ends
running = True
# === GAME LOOP === #
while running:

    clock.tick(SNAKE_SPEED)
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
    #screen.fill(BLACK)
    drawMap(screen)

    snake.draw()
    apple.draw()

    if snake.collision():
        break
    if snake.checkAppleCollision(apple):
        apple.spawn(snake)
    SCORE = len(snake.segments)
    snake.move(apple)
    showScore(SCORE)
    #time.sleep(1/SNAKE_SPEED)
    #snake.move()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
