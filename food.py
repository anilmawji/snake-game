import pygame
import random
from constants import *

x = random.randrange(SCALE, DISPLAY_WIDTH // SCALE)
y = random.randrange(SCALE, DISPLAY_HEIGHT // SCALE)


def move(new_x=0, new_y=0):
    global x, y

    random.seed()
    # Assign random position if one wasn't given
    if new_x == 0:
        new_x = random.randrange(SCALE, DISPLAY_WIDTH // SCALE)
    if new_y == 0:
        new_y = random.randrange(SCALE, DISPLAY_HEIGHT // SCALE)
    x = new_x
    y = new_y


def render(display):
    pygame.draw.circle(display, RED, (x * SCALE + SCALE // 2, y * SCALE + SCALE // 2), SCALE // 2)
