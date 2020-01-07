import pygame

class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, width, height):
        # initialize sprite super class

        # finish setting the class variables to the parameters
        self.main_surface = main_surface

        # Create a surface with the correct height and width
        self.image =

        # Get the rect coordinates
        self.rect =

        # Fill the surface with the correct color

    def move(self):
        pass
