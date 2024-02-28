import pygame
import random
from Settings import *


"""
This module defines the game objects used in the PONG game: player rackets and the ball.

- PLAYER1: Rectangular object representing the first player's racket. It is positioned on the right side of the screen.
- PLAYER2: Rectangular object representing the second player's racket. It is positioned on the left side of the screen.
- BALL: Rectangular object representing the game ball. It starts at the center of the screen.

These objects are initialized with specific positions and dimensions defined by the constants in Settings.py.
The player paddles (PLAYER1 and PLAYER2) are vertical rectangles, while the ball (BALL) is a square.

These objects are used throughout the game loop in Main.py, and their positions are updated based on user input
and the game's logic in the update_objects function in screen.py.

Note: The update_objects function in screen.py also checks for collisions between the ball and paddles,
and it handles the bouncing and scoring logic of the game.
"""


# Отображение игровых объектов(Show game objects)
PLAYER1 = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PLAYER_HEIGHT // 2, PLAYER_WIDTH, PLAYER_HEIGHT)
PLAYER2 = pygame.Rect(10, HEIGHT // 2 - PLAYER_HEIGHT // 2, PLAYER_WIDTH, PLAYER_HEIGHT)
BALL = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
