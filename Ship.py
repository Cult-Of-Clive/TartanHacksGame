import pygame.mixer

from Bullet import Bullet
from Constants import *


class Ship:

    def __init__(self, x, y, color, speed, bullet_num, facing_up):

        self.force_field = False
        self.force_field_uses = 0

        self.speed = speed
        self.num_bullets = bullet_num

        self.bullets = []

        if facing_up:
            self.facing_up = 1
        else:
            self.facing_up = -1

        self.x = x
        self.y = y
        self.color = color

        self.laser_effect = pygame.mixer.Sound(laser_sound_file)

    def ship_coordinates(self):
        base = shipWidth / 2
        return [
            (self.x - base, self.y),
            (self.x + base, self.y),
            (self.x, self.y + self.facing_up * shipHeight)
        ]

    def move_left(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += self.speed
        if self.x > screenSize[0]:
            self.x = screenSize[0]

    def move_down(self):
        self.y += self.speed
        if self.facing_up == -1 and self.y > screenSize[1]:
            self.y = screenSize[1]
        elif self.facing_up == 1 and self.y + shipHeight > 7 * screenSize[1] / 8:
            self.y = 7 * screenSize[1] / 8 - shipHeight

    def move_up(self):
        self.y -= self.speed
        if self.facing_up == -1 and self.y - shipHeight < screenSize[1] / 8:
            self.y = shipHeight + screenSize[1] / 8
        elif self.facing_up == 1 and self.y < 0:
            self.y = 0

    def activate_force_field(self):
        self.force_field = True
        self.force_field_uses = 2

    def draw(self, window):
        pygame.draw.polygon(window, self.color, self.ship_coordinates())
        if self.force_field:
            if self.force_field_uses == 2:
                pygame.draw.circle(window, force_field_color, (self.x, self.y + self.facing_up * shipHeight / 2),
                                   shipHeight, force_field_thickness)
            elif self.force_field_uses == 1:
                pygame.draw.circle(window, force_field_damaged_color,
                                   (self.x, self.y + self.facing_up * shipHeight / 2),
                                   shipHeight, force_field_thickness)
            else:
                self.force_field = False
                self.force_field_uses = 0

        new_bullets = []
        for bullet in self.bullets:
            bullet.draw(window)
            if 0 <= bullet.y <= screenSize[1]:
                new_bullets.append(bullet)
        self.bullets = new_bullets

    def shoot_bullet(self):
        if len(self.bullets) < self.num_bullets:
            bullet = Bullet(self.x, self.y + self.facing_up * shipHeight, self.facing_up * bulletSpeed, self.color)
            self.bullets.append(bullet)
            self.laser_effect.play()
