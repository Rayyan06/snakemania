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

# TODO: MAKE MAP CLASS WITH MAZE
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
GRID_NUM = 50

GRID_WIDTH = SCREEN_SIZE/GRID_NUM
LINE_WIDTH = 0
SNAKE_SPEED = 9

# Colors in the GAME
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
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
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x*GRID_WIDTH, self.y*GRID_WIDTH, GRID_WIDTH, GRID_WIDTH))

    def checkCollision(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

# Fold this up
class Apple(Block):
    color = RED

    def spawn(self, snake):
        self.x = random.randint(0, GRID_NUM-1)
        self.y = random.randint(0, GRID_NUM-1)
        for segment in snake.segments:
            if self.x == segment.x and self.y == segment.y:
                self.x = random.randint(0, GRID_NUM-1)
                self.y = random.randint(0, GRID_NUM-1)

class Snake:
    color = GREEN
    def __init__(self):
        self.spawn()

    def spawn(self):
        self.direction = 'UP'
        self.nextDirection = self.direction

        self.segments = []
        self.x = random.randint(0, GRID_NUM)
        self.y = random.randint(0, GRID_NUM)

        self.length = random.randint(3, 9)

        for block in range(self.length):
            self.segments.append(Block(self.x, self.y-block, self.color))

        self.head = self.segments[0]
    def draw(self):
        for segment in self.segments:
            segment.draw()
            print(segment.x, segment.y)

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

        newBlock = Block(newBlock[0], newBlock[1], self.color)

        self.segments.insert(0, newBlock)

        self.head = self.segments[0]

        if self.checkAppleCollision(apple):
            pass
        else:
            self.segments.pop(-1)

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

class Player(Snake):

    def update(self, keyPressed):
        if keyPressed==K_LEFT:
            self.nextDirection = 'LEFT'
        elif keyPressed == K_UP:
            self.nextDirection = 'UP'
        elif keyPressed == K_DOWN:
            self.nextDirection = 'DOWN'
        elif keyPressed == K_RIGHT:
            self.nextDirection = 'RIGHT'
    def checkEnemyCollision (self, enemy):
        for block in enemy.segments:
            if self.head.checkCollision(block):
                return True

class AI(Snake):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    direction = 'LEFT'


    def __init__(self):
        super().spawn()
    def update(self, apple):

        x = self.head.x
        y = self.head.y


        rand = random.random()

        if rand>x/GRID_NUM:
            self.direction = 'RIGHT'
        if rand<x/ GRID_NUM:
            self.direction = 'LEFT'
        if rand>y/GRID_NUM:
            self.direction = 'DOWN'
        if rand<y / GRID_NUM:
            self.direction = 'UP'

    def checkEnemyCollision(self, enemy):
        for block in enemy.segments:
            if self.head.checkCollision(block):
                return True



        #self.checkEdge()

snakes = []   # All Snakes, including player and AI

player = Player()

for i in range(0, 1):
    snakes.append(AI())

clock = pygame.time.Clock()

apple = Apple(random.randint(0, GRID_NUM), random.randint(0, GRID_NUM), RED)


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

            player.update(event.key)



            print(event.key)

        elif event.type == QUIT:
            running = False

    for snake in snakes:
        snake.update(apple)
    # Fill the Background with BLACK
    #screen.fill(BLACK)
    drawMap(screen)

    for snake in snakes:
        snake.draw()

    player.draw()
    apple.draw()

    for snake in snakes:
        if snake.collision():
            break
        if snake.checkAppleCollision(apple):
            apple.spawn(player)

    if player.collision() or player.checkEnemyCollision(snakes[0]):
        break
    if player.checkAppleCollision(apple):
        apple.spawn(player)

    SCORE = len(player.segments)
    for snake in snakes:
        snake.move(apple)

    player.move(apple)

    showScore(SCORE)
    #time.sleep(1/SNAKE_SPEED)
    #snake.move()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
