# main.py

import pygame
from character import Character
from enemy import Enemy

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("My Game")

# Create character instances
player = Character("player.png", 100, 100, 50, 50)
enemy = Enemy("enemy.png", 200, 200, 60, 60)

# Set the target for the enemy
enemy.set_target(window)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects
    player.update(speed=5)
    enemy.update()
    enemy.chase_player(player)

    # Clear the window
    window.fill((0, 0, 0))

    # Draw game objects
    player.draw(window)
    enemy.draw(window)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()

import pygame
import sys
import random

from character import Character


def create_character(image_path, x, y, width, height, is_enemy=False):
    image = pygame.image.load(image_path)
    scaled_image = pygame.transform.scale(image, (width, height))
    rect = scaled_image.get_rect()
    rect.topleft = (x, y)
    return {
        'image': scaled_image,
        'rect': rect,
        'initial_x': x,
        'initial_y': y,
        'is_enemy': is_enemy,
        'image_path': image_path
    }

def get_random_position(image_width, image_height, window_width, window_height):
    x = random.randint(0, max(0, window_width - image_width))
    y = random.randint(0, max(0, window_height - image_height))
    return x, y

def move_ai_characters(characters, speed, selected_character=None):

    if selected_character is not None:
        for character in characters:
            if character == selected_character:
                continue
            new_x = character['rect'].x + random.choice([-speed, speed])
            new_y = character['rect'].y + random.choice([-speed, speed])

            # Keep the characters within the screen bounds
            character['rect'].x = max(0, min(WINDOWWIDTH - character['rect'].width, new_x))
            character['rect'].y = max(0, min(WINDOWHEIGHT - character['rect'].height, new_y))

            # Append the new position to the trail list
            character_trails[character['image']].append(character['rect'].topleft)

            # Keep only the last 'trail_length' positions
            if len(character_trails[character['image']]) > trail_length:
                character_trails[character['image']].pop(0)


# Initialize Pygame
pygame.init()

# Set up the window width to full screen
WINDOWWIDTH = pygame.display.Info().current_w
WINDOWHEIGHT = pygame.display.Info().current_h

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Super Mario Princess Peach Kingdom')

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the fonts
basicFont = pygame.font.SysFont(None, 48)

# Load images
bowser = pygame.image.load("bowser.webp")
daisy = pygame.image.load("daisy.webp")
mario = pygame.image.load("mario.webp")

shy_guy = pygame.image.load("shy-guy.webp")
bowsers_blimp = pygame.image.load("bowsers-blimp.webp")
goomba = pygame.image.load("goomba.webp")
princess_peach_castle = pygame.image.load("princess-peach-castle.webp")
toad = pygame.image.load("toad.webp")
bowsers_castle = pygame.image.load("bowsers-castle.webp")
koopa_troopa = pygame.image.load("koopa-troopa.webp")
princess_peach = pygame.image.load("princess-peach.webp")
toy_hammer = pygame.image.load("toy-hammer.webp")
daisy_magic_crown = pygame.image.load("daisy-magic-crown.webp")
luigi = pygame.image.load("luigi.webp")
shy_guy_hard = pygame.image.load("shy-guy-hard.webp")

# Scale the images to specific pixel sizes
character_size = (100, 100)  # Specify the desired size for characters
castle_size = (200, 200)  # Specify the desired size for the castle

daisy_size = (100, 150)

shy_guy = pygame.transform.scale(shy_guy, character_size)
shy_guy_hard = pygame.transform.scale(shy_guy_hard, character_size)
koopa_troopa = pygame.transform.scale(koopa_troopa, character_size)
goomba = pygame.transform.scale(goomba, character_size)
princess_peach_castle = pygame.transform.scale(princess_peach_castle, castle_size)
bowsers_castle = pygame.transform.scale(bowsers_castle, castle_size)
toad = pygame.transform.scale(toad, character_size)
mario = pygame.transform.scale(mario, character_size)
daisy = pygame.transform.scale(daisy, daisy_size)
princess_peach = pygame.transform.scale(princess_peach, character_size)

#rotate princess_peach 90 degrees clockwise
princess_peach = pygame.transform.rotate(princess_peach, -90)

toy_hammer = pygame.transform.scale(toy_hammer, character_size)
daisy_magic_crown = pygame.transform.scale(daisy_magic_crown, character_size)
luigi = pygame.transform.scale(luigi, character_size)
bowsers_blimp = pygame.transform.scale(bowsers_blimp, (200, 200))
bowser = pygame.transform.scale(bowser, character_size)

trail_colors = {
    "mario.webp": (255, 0, 0),  # Red
    "luigi.webp": (0, 255, 0),  # Green
    "princess-peach.webp": (255, 192, 203),  # Pink
    "toad.webp": (255, 165, 0),  # Orange
    "daisy.webp": (255, 255, 0),  # Yellow
    "shy-guy.webp": (255, 0, 255),  # Magenta
    "shy-guy-hard.webp": (128, 0, 128),  # Purple
    "koopa-troopa.webp": (0, 255, 255),  # Cyan
    "goomba.webp": (165, 42, 42)  # Brown
}



# Set up the text
text = basicFont.render('Welcome to Super Mario Princess Peach Kingdom', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Draw the background and shapes
windowSurface.fill(WHITE)
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# Pixel manipulation (do this before locking issues can occur)
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray  # Immediately unlock the surface after modification

# Draw the text onto the surface (ensure this is done after pixel array is deleted)
windowSurface.blit(text, textRect)

# Draw the characters and objects
bowswer_castle_x = 50
bowser_castle_y = WINDOWHEIGHT - 1.5 * bowsers_castle.get_height()


princess_peach_castle_x = WINDOWWIDTH - princess_peach_castle.get_width() - 50
princess_peach_castle_y = WINDOWHEIGHT - 1.5 * princess_peach_castle.get_height()
windowSurface.blit(princess_peach_castle, (princess_peach_castle_x, princess_peach_castle_y))
windowSurface.blit(bowser, (100, WINDOWHEIGHT - bowsers_castle.get_height() - bowser.get_height()))
windowSurface.blit(bowsers_blimp, (150, WINDOWHEIGHT - bowsers_castle.get_height() - bowser.get_height() - bowsers_blimp.get_height()))

#character y position is the bottom of the window minus 1.5 times the character height
character_y = WINDOWHEIGHT - 1.5 * mario.get_height()
#mario is in the middle of the window
mario_x = WINDOWWIDTH // 2 - mario.get_width() // 2
daisy_x = mario_x + daisy.get_width()
luigi_x = mario_x + 2 * luigi.get_width()
toad_x = mario_x + 3 * toad.get_width()
princess_peach_x = mario_x - princess_peach.get_width()

daisy_y = WINDOWHEIGHT - 1.5 * daisy.get_height()

windowSurface.blit(mario, (mario_x, character_y))
windowSurface.blit(daisy, (daisy_x, daisy_y))
windowSurface.blit(luigi, (luigi_x, character_y))
windowSurface.blit(toad, (toad_x, character_y))
windowSurface.blit(princess_peach, (princess_peach_x, character_y))



windowSurface.blit(daisy_magic_crown, (WINDOWWIDTH // 2 - daisy_magic_crown.get_width() // 2, 50))

#place toy hammer inside of princess_peach_castle
#x position is the center of the castle minus half of the toy hammer width
toy_hammer_x = princess_peach_castle_x + princess_peach_castle.get_width() // 2 - toy_hammer.get_width() // 2
#y position is the bottom of the castle minus half of the toy hammer height
toy_hammer_y = princess_peach_castle_y + princess_peach_castle.get_height() - toy_hammer.get_height() // 2
windowSurface.blit(toy_hammer, (toy_hammer_x, toy_hammer_y))

 # Draw the images at random positions
shy_guy_x, shy_guy_y = get_random_position(shy_guy.get_width(), shy_guy.get_height(), WINDOWWIDTH, WINDOWHEIGHT)
windowSurface.blit(shy_guy, (shy_guy_x, shy_guy_y))

shy_guy_hard_x, shy_guy_hard_y = get_random_position(shy_guy_hard.get_width(), shy_guy_hard.get_height(), WINDOWWIDTH, WINDOWHEIGHT)
windowSurface.blit(shy_guy_hard, (shy_guy_hard_x, shy_guy_hard_y))

koopa_troopa_x, koopa_troopa_y = get_random_position(koopa_troopa.get_width(), koopa_troopa.get_height(), WINDOWWIDTH, WINDOWHEIGHT)
windowSurface.blit(koopa_troopa, (koopa_troopa_x, koopa_troopa_y))

goomba_x, goomba_y = get_random_position(goomba.get_width(), goomba.get_height(), WINDOWWIDTH, WINDOWHEIGHT)
windowSurface.blit(goomba, (goomba_x, goomba_y))



# Create a list to store playable characters
playable_characters = [
    create_character("mario.webp", mario_x, character_y, 40, 64),
    create_character("luigi.webp", luigi_x, character_y, 40, 64),
    create_character("princess-peach.webp", princess_peach_x, character_y, 40, 64),
    create_character("toad.webp", toad_x, character_y, 40, 64),
    create_character("daisy.webp", daisy_x, daisy_y, 62, 104)
]

enemy_characters = [
    create_character("shy-guy.webp", shy_guy_x, shy_guy_y, 35, 36, is_enemy=True),
    create_character("shy-guy-hard.webp", shy_guy_hard_x, shy_guy_hard_y, 30, 39, is_enemy=True),
    create_character("koopa-troopa.webp", koopa_troopa_x, koopa_troopa_y, 35, 40, is_enemy=True),
    create_character("goomba.webp", goomba_x, goomba_y, 30, 30, is_enemy=True)
]


selected_character = None

# Update the display
pygame.display.update()


elipse_x = 300
elipse_y = 250

#play Kings-of-Freedom.mp3 water-splash.mp3 as the background music
pygame.mixer.music.load('Kings-of-Freedom.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)


# Store the trails for each character

character_trails = {char['image']: [] for char in playable_characters + enemy_characters}

trail_length = 10  # how many steps the trail will display



def move_selected_character_with_mouse(selected_character):
    # Get the trail color and size for the selected character
    trail_color = trail_colors.get(selected_character['image'], (0, 0, 0))
    trail_size = selected_character['image'].get_size()

    # Update the position of the selected character to where the mouse is
    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_character['rect'].center = (mouse_x, mouse_y)

    # Append the new position to the trail list
    character_trails[selected_character['image']].append(selected_character['rect'].topleft)

    # Keep only the last 'trail_length' positions
    if len(character_trails[selected_character['image']]) > trail_length:
        character_trails[selected_character['image']].pop(0)

    # Draw the trail
    for position in character_trails[selected_character['image']]:
        pygame.draw.rect(windowSurface, trail_color, (position[0], position[1], *trail_size))

# Then, in your main game loop, where you currently have:
if selected_character is not None:
    selected_character['rect'].center = pygame.mouse.get_pos()
# replace it with:
if selected_character is not None:
    move_selected_character_with_mouse(selected_character)



for character in playable_characters:
    trail_color = trail_colors.get(character['image'], (0, 0, 0))
    trail_size = character['image'].get_size()
    for position in character_trails[character['image']]:
        pygame.draw.rect(windowSurface, trail_color, pygame.Rect(position, trail_size))

# Blit the characters after drawing the trails
for character in playable_characters:
    windowSurface.blit(character['image'], character['rect'])

# Clear the screen before drawing anything, to remove the old images and trails
windowSurface.fill(WHITE)  # Assuming WHITE is your background color


def check_castle_collisions(character):
    if character['rect'].colliderect(pygame.Rect(bowswer_castle_x, bowser_castle_y, bowsers_castle.get_width(), bowsers_castle.get_height())):
        # Character collided with Bowser's Castle
        character['rect'].topleft = (character['initial_x'], character['initial_y'])  # Reset character position
        character_trails[character['image']].clear()  # Remove character's trails
        # Decrement lives or perform other actions
    elif character['rect'].colliderect(pygame.Rect(princess_peach_castle_x, princess_peach_castle_y, princess_peach_castle.get_width(), princess_peach_castle.get_height())):
        # Character collided with Princess Peach's Castle
        character['rect'].topleft = (character['initial_x'], character['initial_y'])  # Reset character position
        character_trails[character['image']].clear()  # Remove character's trails
        # Decrement lives or perform other actions

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for character in playable_characters:
                    if character['rect'].collidepoint(event.pos):
                        selected_character = character
                        break
        # And finally, clear the trails when the character is not selected
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                if selected_character:
                    character_trails[selected_character['image']].clear()
                selected_character = None

    # Move the selected character with the mouse
    if selected_character is not None:
        selected_character['rect'].center = pygame.mouse.get_pos()

    # Move the selected character with the arrow keys
    if selected_character is not None:
       move_selected_character_with_mouse(selected_character)

    # Move the AI-controlled playable characters
    if(selected_character is not None):
        move_ai_characters(playable_characters, speed=5, selected_character=selected_character)

    


    # Draw the playable characters
    for character in playable_characters:
        windowSurface.blit(character['image'], character['rect'])

    # Move the ellipse
    pygame.draw.ellipse(windowSurface, RED, (elipse_x, elipse_y, 40, 80), 1)
    pygame.draw.ellipse(windowSurface, WHITE, (elipse_x - 1, elipse_y - 1, 42, 82), 1)

    # Redraw the textbox on top of the ellipse
    windowSurface.blit(text, textRect)

    elipse_x += 1
    elipse_y += 1
    if elipse_x > 400:
        elipse_x = 300

    if elipse_y > 350:
        elipse_y = 250

    # Drawing
    #windowSurface.fill(WHITE)
    #DISPLAYSURF.blit(background_image, (0, 0))
    windowSurface.blit(bowsers_castle, (bowswer_castle_x, bowser_castle_y))
    windowSurface.blit(princess_peach_castle, (princess_peach_castle_x, princess_peach_castle_y))

    # Draw trails for playable characters
    for character in playable_characters:
        for i, pos in enumerate(character_trails[character['image']]):
            color = trail_colors[character['image_path']]
            #pygame.draw.rect(windowSurface, color, pos, (character['image'].get_size()))
            pygame.draw.rect(windowSurface, color, character.rect, 2)

    # Draw trails for enemy characters
    """
    for enemy in enemy_characters:
        for i, pos in enumerate(enemy_trails[enemy['image']]):
            color = trail_colors[enemy['image']]
            pygame.draw.circle(windowSurface, color, pos, 5)
    """
    # Draw playable characters
    for character in playable_characters:
        windowSurface.blit(character['image'], character['rect'])

    # Draw enemy characters
    for enemy in enemy_characters:
        windowSurface.blit(enemy['image'], enemy['rect'])
        for character in playable_characters:
            check_castle_collisions(character)

    pygame.display.update()