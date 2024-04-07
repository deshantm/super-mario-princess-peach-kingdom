# enemy.py

import pygame
from constants import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2  # Add this line to define the speed attribute

    def chase_player(self, player):
        if player is not None:
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance > 0:
                speed = min(self.speed, distance)
                self.rect.x += int(dx / distance * speed)
                self.rect.y += int(dy / distance * speed)

    def draw(self, surface):
        surface.blit(self.image, self.rect)