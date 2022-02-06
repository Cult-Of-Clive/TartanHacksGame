import pygame
from Constants import *


class Bullet:

    # Bullet constructor
    def __init__(self, x, y, velocity, color):
        self.x = x
        self.y = y
        self.velocity = velocity

        self.width = bulletWidth
        self.color = color

    # Get a list of coordinates for the bullet's vertices
    def bullet_coordinates(self):
        # (x,y) represent southwest corner of square
        base = self.width / 2
        return [
            (self.x + base, self.y + self.width),
            (self.x - base, self.y + self.width),
            (self.x - base, self.y),
            (self.x + base, self.y)
        ]

    # Draw and move the bullet
    def draw(self, window):
        pygame.draw.polygon(window, self.color, self.bullet_coordinates())
        self.move()

    # Move the bullet
    def move(self):
        self.y += self.velocity
