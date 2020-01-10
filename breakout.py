import pygame , sys
from pygame.locals import *
import brick
import paddle
import ball

pygame.init()


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

    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    main_surface.fill(WHITE)

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)

    x_pos = BRICK_SEP
    y_pos = BRICK_Y_OFFSET
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
    y_pos_paddle = APPLICATION_HEIGHT - PADDLE_Y_OFFSET

    my_paddle = paddle.Paddle(main_surface, BLACK, PADDLE_WIDTH, PADDLE_HEIGHT)
    main_surface.blit(my_paddle.image, (x_pos_paddle, y_pos_paddle))
    paddle_group.add(my_paddle)

    my_ball = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    my_ball.rect.x = APPLICATION_WIDTH/2
    my_ball.rect.y = APPLICATION_HEIGHT/2
    main_surface.blit(my_ball.image, my_ball.rect)

    while True:
        main_surface.fill(WHITE)
        for a_brick in bricks_group:
            main_surface.blit(a_brick.image, a_brick.rect)
        my_paddle.move(pygame.mouse.get_pos())
        main_surface.blit(my_paddle.image, (my_paddle.rect.x, y_pos_paddle))
        main_surface.blit(my_ball.image, (my_ball.rect.x, my_ball.rect.y))
        my_ball.move()
        pygame.display.update()
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()


main()
