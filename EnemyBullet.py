import math
import random

import pygame
from Constants import *


class EnemyBullet:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        theta = random.randint(0, 360)

        self.x_vel = enemyBulletSpeed*math.cos(theta)
        self.y_vel = enemyBulletSpeed*math.sin(theta)

        self.width = bulletWidth
        self.color = enemyColor

    def bullet_coordinates(self):
        # (x,y) represent southwest corner of square
        base = self.width / 2
        return [
            (self.x + base, self.y + self.width),
            (self.x - base, self.y + self.width),
            (self.x - base, self.y),
            (self.x + base, self.y)
        ]

    def draw(self, window):
        pygame.draw.polygon(window, self.color, self.bullet_coordinates())
        self.move()

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

