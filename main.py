# main.py

import pygame
from pygame import mixer
from character import Character
from enemy import Enemy
from constants import *

def setup_characters():
    CHARACTER_WIDTH = 50
    CHARACTER_HEIGHT = 50

    mario_image = pygame.image.load("mario.webp")
    mario_image = pygame.transform.scale(mario_image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    luigi_image = pygame.image.load("luigi.webp")
    luigi_image = pygame.transform.scale(luigi_image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    daisy_image = pygame.image.load("daisy.webp")
    daisy_image = pygame.transform.scale(daisy_image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    peach_image = pygame.image.load("princess-peach.webp")
    peach_image = pygame.transform.scale(peach_image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    toad_image = pygame.image.load("toad.webp")
    toad_image = pygame.transform.scale(toad_image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    bowser_image = pygame.image.load("bowser.webp")
    bowser_image = pygame.transform.scale(bowser_image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

    mario = Character(mario_image, 100, 100)
    luigi = Character(luigi_image, 200, 100)
    daisy = Character(daisy_image, 300, 100)
    peach = Character(peach_image, 400, 100)
    toad = Character(toad_image, 500, 100)
    bowser = Enemy(700, 100, CHARACTER_WIDTH, CHARACTER_HEIGHT, RED)

    return mario, luigi, daisy, peach, toad, bowser

def setup_castles():
    bowsers_castle = pygame.Rect(50, 50, 100, 100)
    princess_peach_castle = pygame.Rect(WINDOWWIDTH - 150, WINDOWHEIGHT - 150, 100, 100)
    return bowsers_castle, princess_peach_castle

def main():
    pygame.init()
    mixer.init()
    mixer.music.load("Kings-of-Freedom.mp3")
    mixer.music.play(-1)

    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Super Mario: Princess Peach's Kingdom")

    mario, luigi, daisy, peach, toad, bowser = setup_characters()
    bowsers_castle, princess_peach_castle = setup_castles()

    trail_colors = {
        mario: RED,
        luigi: GREEN,
        daisy: ORANGE,
        peach: PINK,
        toad: WHITE
    }

    for character, color in trail_colors.items():
        character.trail_color = color

    selected_character = None

    clock = pygame.time.Clock()

    trail_surface = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT), pygame.SRCALPHA)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if selected_character is None:
                    for character in [mario, luigi, daisy, peach, toad]:
                        if character.rect.collidepoint(event.pos):
                            selected_character = character
                            break
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_character = None

        if selected_character:
            mouse_pos = pygame.mouse.get_pos()
            selected_character.rect.centerx = mouse_pos[0]
            selected_character.rect.centery = mouse_pos[1]

        for character in [mario, luigi, daisy, peach, toad]:
            if character != selected_character:
                character.move_ai(3, WINDOWWIDTH, WINDOWHEIGHT)

        bowser.chase_player(selected_character)

        for character in [mario, luigi, daisy, peach, toad]:
            character.check_castle_collisions(bowsers_castle, princess_peach_castle)

        #trail_surface.fill((0, 0, 0, 0))  # Clear the trail surface

        for character in [mario, luigi, daisy, peach, toad]:
            character.update()
            character.draw_trail(trail_surface, [bowsers_castle, princess_peach_castle])

        window.fill(WHITE)

        pygame.draw.rect(window, RED, bowsers_castle)
        pygame.draw.rect(window, PINK, princess_peach_castle)

        bowser.draw(window)

        window.blit(trail_surface, (0, 0))  # Draw the trail surface on the main window

        for character in [mario, luigi, daisy, peach, toad]:
            character.draw(window)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()