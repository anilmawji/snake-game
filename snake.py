import pygame
import math
from constants import *


class Snake:

    def __init__(self, x=DISPLAY_WIDTH // 2 // SCALE, y=DISPLAY_HEIGHT // 2 // SCALE, color=GREEN, size=START_SIZE):
        self.x = x
        self.y = y
        self.speed = 1
        self.direction = RIGHT
        self.segments = []
        self.color = color
        self.init_segments(size)
        self.dead = False

    def init_segments(self, size):
        self.segments = [(self.x, self.y)]

        if size > 1:
            for i in range(1, size):
                self.segments.insert(0, (self.x - i, self.y))

    def tick(self):
        if self.dead:
            self.dead = False

        # Move in current direction
        if self.direction == RIGHT:
            self.x += self.speed
        elif self.direction == LEFT:
            self.x -= self.speed
        elif self.direction == UP:
            self.y -= self.speed
        elif self.direction == DOWN:
            self.y += self.speed

        # Shift snake segments for movement
        num_segments = len(self.segments)
        for i in range(num_segments - 1):
            self.segments[i] = self.segments[i + 1]
        self.segments[-1] = (self.x, self.y)

        # Check for collision with bounds of screen
        if self.x < 0 or self.x > DISPLAY_WIDTH // SCALE - 1 or self.y < 0 or self.y > DISPLAY_HEIGHT // SCALE - 1:
            self.die()
        elif num_segments > 3:
            # Check for collision with self
            for pos in self.segments[:-1]:
                if math.dist(self.segments[-1], pos) < 1:
                    self.die()
                    break

    def render(self, display):
        for pos in self.segments:
            pygame.draw.rect(display, self.color, (pos[0] * SCALE, pos[1] * SCALE, SCALE, SCALE))

    def grow(self, amount=1):
        # Insert new segments into the snake
        for i in range(amount):
            self.segments.insert(0, (self.x, self.y))

    def die(self):
        self.dead = True
        # Reset fields
        self.x = DISPLAY_WIDTH // 2 // SCALE
        self.y = DISPLAY_HEIGHT // 2 // SCALE
        self.speed = 1
        self.direction = RIGHT
        self.init_segments(START_SIZE)

    def collides_with(self, x, y):
        # Check each snake segment for a collision
        for pos in self.segments:
            if pos[0] == x and pos[1] == y:
                return True
        return False

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def is_dead(self):
        return self.dead
