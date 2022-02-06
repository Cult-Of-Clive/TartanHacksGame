import math

import pygame.draw

from Constants import *
import random


class Powerup:
    def __init__(self):
        self.color = (0, 0, 0)
        self.entry_side = random.randint(0, 2)

        angle = random.randint(-45, 46)

        self.x_vel = powerupSpeed*math.cos(math.radians(angle))
        self.y_vel = powerupSpeed*math.sin(math.radians(angle))

        # Left Side
        if self.entry_side == 0:
            self.x = 0
        else:
            self.x = screenSize[0]
            self.x_vel *= -1

        self.y = random.randint(0, screenSize[1])

    def draw(self, screen):
        pygame.draw.circle(screen, powerupColor, (self.x, self.y), powerupRadius, powerupThickness)
        pygame.draw.circle(screen, self.color, (self.x, self.y), powerupRadius - powerupThickness)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

        if self.x < 0 or self.x > screenSize[0]:
            self.x_vel = -self.x_vel
        if self.y < 0 or self.y > screenSize[1]:
            self.y_vel = -self.y_vel

    def take_red_damage(self, damage):
        red, green, blue = self.color

        if green == 0:
            red += damage
            if red > 255:
                red = 255
        else:
            green -= damage
            if green < 0:
                green = 0
        self.color = (red, green, blue)

    def take_green_damage(self, damage):
        red, green, blue = self.color

        if red == 0:
            green += damage
            if green > 255:
                green = 255
        else:
            red -= damage
            if red < 0:
                red = 0
        self.color = (red, green, blue)
