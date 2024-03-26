import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
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

# Draw the window onto the screen
pygame.display.update()

elipse_x = 300
elipse_y = 250

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #move the elipse
            
   
            
    #use parameters to move the elipse
    pygame.draw.ellipse(windowSurface, RED, (elipse_x, elipse_y, 40, 80), 1)
    #remove previous elipse
    pygame.draw.ellipse(windowSurface, WHITE, (elipse_x - 1, elipse_y - 1, 42, 82), 1)


    #redraw the textbox on top of the elipse
    windowSurface.blit(text, textRect)
    #update the display
    


    elipse_x += 1
    elipse_y += 1
    if elipse_x > 400:
        elipse_x = 300


    if elipse_y > 350:
        elipse_y = 250

    
    pygame.display.update()

    # Game loop logic here. Avoid creating/deleting PixelArray unless necessary.
    # Update display only if needed to avoid unnecessary performance hit.
    # pygame.display.update() could be called here if you're making changes that need to be displayed in real-time.
