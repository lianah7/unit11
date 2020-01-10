import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, width, height):
        # initialize sprite super class
        super().__init__()
        self.color = color
        self.width = width
        self.height = height

        # finish setting the class variables to the parameters
        self.main_surface = main_surface

        # Create a surface with the correct height and width
        self.image = pygame.Surface((width, height))

        # Get the rect coordinates
        self.rect = self.image.get_rect()

        # Fill the surface with the correct color
        self.image.fill(color)

    def move(self, position):
        self.rect.x = position[0]




