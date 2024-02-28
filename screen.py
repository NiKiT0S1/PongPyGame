import pygame
import sys
from Settings import *
from Ball_and_Players import *


"""
The screen module, screen.py, handles the graphical aspects of the PONG game.
- It defines colors and provides functions to draw game objects on the screen.
- The screen_objects function draws the rackets, ball, and the score display.
- The update_objects function updates the position of the ball, checks for collisions,
  and handles scoring and game-end conditions.
- Additionally, there is a reset_game function to reset the game state after a goal is scored.
"""



# Цветовая гамма(Colors)
WHITE = (255, 255, 255)
BLACK = (120, 0, 120)

# Функция отрисовки объектов(Draw game objects function)
def screen_objects(screen):
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, PLAYER1)
    pygame.draw.rect(screen, WHITE, PLAYER2)
    pygame.draw.ellipse(screen, WHITE, BALL)

    # Отображение счета(Show the score)
    font = pygame.font.Font(None, 65)
    score_display = font.render(f"{score_p1} - {score_p2}", True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - 50, 10))

# Обновление положения мяча(Update the position of the ball)
def update_objects():
    global ball_speed_x, ball_speed_y, score_p1, score_p2, SCORE_LIMIT

    BALL.x += ball_speed_x
    BALL.y += ball_speed_y

    # Отскок от верхней и нижней границ(Bounce off top and bottom boundaries)
    if BALL.top <= 0 or BALL.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Отскок от ракеток(Bounce off rackets)
    if BALL.colliderect(PLAYER1):
        ball_speed_x = -ball_speed_x
    elif BALL.colliderect(PLAYER2):
        ball_speed_x = -ball_speed_x

    # Проверка забития гола(Check for goals)
    if BALL.left <= 0:
        score_p2 = score_p2+1
        reset_game()
    elif BALL.right >= WIDTH:
        score_p1 += 1
        reset_game()

    # Проверка на окончание игры(Check the end of game)
    if score_p1 == SCORE_LIMIT or score_p2 == SCORE_LIMIT:
        pygame.quit()
        sys.exit()


# Функция сброса положения мяча после гола(Reset the game after goal function)
def reset_game():
    global ball_speed_x, ball_speed_y, score_p1, score_p2
    BALL.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x = random.choice([-8, 8])
    ball_speed_y = random.choice([-8, 8])
