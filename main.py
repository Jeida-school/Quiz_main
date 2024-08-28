# Import pygame so that we can access its code
import pygame as p
from pygame import image as img

# Initialise/activate pygame
p.init()

# Set the size of the display window
screen_size = ((500, 500))
win = p.display.set_mode((screen_size))

# Setting the time in the game so that I can use it to run the game
clock = p.time.Clock()

# Main game loop
while True:
    # fps set to 60
    clock.tick(60)

    