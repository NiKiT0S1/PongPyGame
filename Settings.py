import random

"""
The Settings module, Settings.py, defines various parameters and configurations for the PONG game.
- WIDTH, HEIGHT: Define the resolution of the game window.
- PLAYER_WIDTH, PLAYER_HEIGHT: Specify the dimensions of the player paddles.
- BALL_SIZE: Sets the size of the game ball.
- FPS: Determines the frames per second for the game loop.
- SCORE_LIMIT: Sets the maximum score needed to win the game.
- ball_speed_x, ball_speed_y: Define the initial speed of the ball along the x and y axes.
- score_p1, score_p2: Keep track of the scores for player 1 and player 2.
"""




"""
# Разрешение игры, размер ракеток игроков и мяча, количество кадров и раундов
# Game resolution, player and ball sizes, frame rate and score limit
"""
WIDTH, HEIGHT = 1280, 720
PLAYER_WIDTH, PLAYER_HEIGHT = 20, 150
BALL_SIZE = 20
FPS = 60
SCORE_LIMIT = 10

# Скорости мяча(Ball speeds)
ball_speed_x = random.choice([-8, 8])
ball_speed_y = random.choice([-8, 8])

# Счетчик очков игроков(Score for players)
score_p1 = 0
score_p2 = 0





