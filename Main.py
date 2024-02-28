import random
import pygame
import sys
from Settings import *
from Ball_and_Players import *
from screen import update_objects
from Players_Control import move_player1, move_player2
from screen import screen_objects


"""
This is the main script, Main.py, responsible for running the PONG game.
- It initializes the game window using Pygame.
- The game loop captures events, such as quitting the game, and handles player input.
- Player movement is controlled using the functions from Players_Control.
- The game objects are updated using the update_objects function from the screen module.
- The game state is displayed on the screen using the screen_objects function from the screen module.
- The game loop continues until an unexpected error occurs, after which the game is gracefully exited.
"""




# Инициализация Pygame(Initialize pygame)
pygame.init()

try:
    # Создание окна(Create the window)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PONG (1972)")


    # Игровой цикл(Game loop)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Скорость управление игроками(Player control handling)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            move_player1(-10)
        if keys[pygame.K_DOWN]:
            move_player1(10)

        if keys[pygame.K_w]:
            move_player2(-10)
        if keys[pygame.K_s]:
            move_player2(10)

        update_objects()

        # Отображение игровых объектов на экране(Show game objects on the screen)
        screen_objects(screen)

        pygame.display.flip()
        clock.tick(FPS)
except Exception:
    print("Some unexpected error occurred in the code")
    pygame.quit()
    sys.exit()



