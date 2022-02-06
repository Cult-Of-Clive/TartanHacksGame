import random
import math
import time

import pygame.draw_py

from EnemyBullet import EnemyBullet
from Constants import *


# Enemy Class
class Enemy:
    def __init__(self):
        self.max_bullet_num = enemyBullets
        self.bullets = []
        self.health = enemyHealth
        self.alive = True

        self.entry_side = random.randint(0, 2)

        angle = random.randint(-45, 46)

        self.x_vel = powerupSpeed * math.cos(math.radians(angle))
        self.y_vel = powerupSpeed * math.sin(math.radians(angle))
        self.theta = random.randint(0, 360)

        self.rotation_speed = enemyRotationSpeed

        # Left Side
        if self.entry_side == 0:
            self.x = 0
        else:
            self.x = screenSize[0]
            self.x_vel *= -1

        self.y = random.randint(0, screenSize[1])
        self.laser_effect = pygame.mixer.Sound(laser_sound_file)

    def get_square(self):
        cos_theta = math.cos(math.radians(self.theta))
        sin_theta = math.sin(math.radians(self.theta))
        return [
            (self.x - enemyRadius * cos_theta, self.y + enemyRadius * sin_theta),
            (self.x - enemyRadius * cos_theta, self.y - enemyRadius * sin_theta),
            (self.x + enemyRadius * cos_theta, self.y + enemyRadius * sin_theta),
            (self.x + enemyRadius * cos_theta, self.y - enemyRadius * sin_theta)
        ]

    def draw(self, screen):
        pygame.draw.circle(screen, enemyColor, (self.x, self.y), enemyRadius, enemyThickness)
        pygame.draw.polygon(screen, enemyColor, self.get_square())
        self.move()
        new_bullets = []
        for bullet in self.bullets:
            bullet.draw(screen)
            if 0 <= bullet.y <= screenSize[1]:
                new_bullets.append(bullet)
        self.bullets = new_bullets

    def shoot_bullet(self):
        if len(self.bullets) < self.max_bullet_num:
            bullet = EnemyBullet(self.x, self.y)
            self.bullets.append(bullet)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

        if self.x < 0 or self.x > screenSize[0]:
            self.x_vel = -self.x_vel
        if self.y < 0 or self.y > screenSize[1]:
            self.y_vel = -self.y_vel

        self.theta += self.rotation_speed
        self.theta = self.theta % 360

    def take_damage(self):
        self.health -= 1
        self.rotation_speed += enemyRotationSpeedIncrement
        self.max_bullet_num += enemyBulletIncrement
        if self.health <= 0:
            self.alive = False
