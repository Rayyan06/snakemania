#! usr/bin/python3
# main.py -- main file
# Import Pygame
import pygame

# Initialize Pygame functions
pygame.init()


# setup our screen to draw on
# The size of our screen, the width and the height (width=height)
SCREEN_SIZE = 500
# Create the screen
screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])

# Colors in the GAME
BLACK = (0, 0, 0)

# Run until game ends
running = True
# === GAME LOOP === #
while running:

    # Check every event in the event list
    for event in pygame.event.get():
        # If the event is pygame.QUIT(user closed window)...
        if event.type == pygame.QUIT:
            # ... then quit the game
            running = False

    # Fill the Background with BLACK
    screen.fill(BLACK)

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
