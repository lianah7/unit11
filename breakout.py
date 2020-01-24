# by Liana Hill
# last modified January 24, 2020
# unit 11 Breakout Project


import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball

pygame.init()


# Creates a screen that tells the user they won the game
# Fills main surface with new color and displays a label telling the user they won
def you_win(main_surface):
    main_surface.fill((255, 99, 71))
    my_font = pygame.font.SysFont("Helvetica", 68)
    label = my_font.render("YOU WIN", 1, (255, 255, 255))
    main_surface.blit(label, (90, 250))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()


# Creates a screen that tells the user they lost the game
# Fills main surface with new color and displays label telling the user they lost
def you_lose(main_surface):
    main_surface.fill((72, 118, 255))
    my_font = pygame.font.SysFont("Helvetica", 64)
    label = my_font.render("YOU LOSE", 1, (255, 255, 255))
    main_surface.blit(label, (90, 245))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()


def main():
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    colors = [RED, ORANGE, YELLOW, GREEN, CYAN]

    bricks_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()

    # Sets downloaded photo as background image
    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    bg = pygame.image.load("backyard.jpg")
    main_surface.blit(bg, (0, 0))
    # main_surface.fill(WHITE)

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)
    x_pos = BRICK_SEP
    y_pos = BRICK_Y_OFFSET

    # Colors bricks different colors every second row
    # Draws bricks onto main surface in rows and columns with specific measurements
    for hue in colors:
        for y in range(2):
            for x in range(BRICKS_PER_ROW):
                my_brick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, hue)
                my_brick.rect.x = x_pos
                my_brick.rect.y = y_pos
                bricks_group.add(my_brick)
                main_surface.blit(my_brick.image, (x_pos, y_pos))
                x_pos += BRICK_WIDTH + BRICK_SEP
            y_pos += BRICK_HEIGHT + BRICK_SEP
            x_pos = BRICK_SEP

    x_pos_paddle = 200

    # Creates paddle with specific measurements and blit the paddle onto the main surface
    my_paddle = paddle.Paddle(main_surface, BLACK, PADDLE_WIDTH, PADDLE_HEIGHT)
    my_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    main_surface.blit(my_paddle.image, my_paddle.rect)
    paddle_group.add(my_paddle)

    # Creates ball with specific measurements and blits ball onto main surface
    my_ball = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    my_ball.rect.x = APPLICATION_WIDTH/2
    my_ball.rect.y = APPLICATION_HEIGHT/2
    main_surface.blit(my_ball.image, my_ball.rect)

    tries = 0

    while True:
        # Draws bricks onto screen after screen is blanked out
        # Only bricks that have not collided with ball will appear on screen
        main_surface.blit(bg, (0, 0))
        for a_brick in bricks_group:
            main_surface.blit(a_brick.image, a_brick.rect)

        # Moves the paddle based on the movement of the user's mouse
        my_paddle.move(pygame.mouse.get_pos())
        main_surface.blit(my_paddle.image, my_paddle.rect)
        main_surface.blit(my_ball.image, my_ball.rect)

        #  Moves ball based on collisions with bricks and paddle
        my_ball.move()
        my_ball.collide(paddle_group)
        my_ball.collide_brick(bricks_group)

        # Reblits ball onto main surface after it collides with the bottom of screen
        # Adds one to the number of tries
        if my_ball.rect.bottom >= APPLICATION_HEIGHT:
            my_ball.rect.x = APPLICATION_WIDTH/2
            my_ball.rect.y = APPLICATION_HEIGHT/2
            tries += 1

        # Displays screen that states the user lost if the ball hits the bottom of the screen three times
        if tries == 3:
            you_lose(main_surface)

        # Displays screen that states the user won if all the bricks have been hit
        if len(bricks_group) == 0:
            you_win(main_surface)
        pygame.display.update()
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()


main()
