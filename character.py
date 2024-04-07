# character.py

import pygame
import random
from game_object import GameObject

class Character(GameObject):
    def __init__(self, image, x, y):
        super().__init__(image, x, y, image.get_width(), image.get_height())
        self.speed = 5
        self.trail_color = None

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, surface):
        super().draw(surface)

    def draw_trail(self, trail_surface, castle_props):
        if self.trail_color is not None:
            if not any(self.rect.colliderect(prop) for prop in castle_props):
                pygame.draw.rect(trail_surface, self.trail_color, self.rect)

    def check_castle_collisions(self, bowsers_castle, princess_peach_castle):
        if self.rect.colliderect(bowsers_castle):
            print("Collision with Bowser's Castle!")
        elif self.rect.colliderect(princess_peach_castle):
            print("Collision with Princess Peach's Castle!")

    def move_with_mouse(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.centerx = mouse_pos[0]
        self.rect.centery = mouse_pos[1]

    def move_ai(self, speed, max_x, max_y):
        self.rect.x += random.randint(-speed, speed)
        self.rect.y += random.randint(-speed, speed)
        self.rect.clamp_ip(pygame.Rect(0, 0, max_x, max_y))