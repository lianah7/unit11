import pygame, sys
from pygame.locals import *
import circle

# Fills and creates measurements for screen
pygame.init()
main_surface = pygame.display.set_mode((500, 400), 0, 32)
main_surface.fill((255, 255, 255))

# Creates a circle for ball, sets position, and blits onto main surface
new_circle = circle.Circle(main_surface)
new_circle.rect.x = 250
new_circle.rect.y = 200
main_surface.blit(new_circle.image, new_circle.rect)  # what and where


while True:
    # Process of loop: fill surface, move shape, blit shape, update
    main_surface.fill((255, 255, 255))
    new_circle.move()
    main_surface.blit(new_circle.image, new_circle.rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()