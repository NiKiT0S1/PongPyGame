#ЖЕНИС

# Игровой процесс

import pygame
import sys
from Ball_and_Players import *
from Settings import *
from screen import screen_objects


# Инициализация
#pygame.init()

# # Обновление положения мяча (Ball_and_Players)
# def update_objects():
#     global ball_speed_x, ball_speed_y, score_p1, score_p2
#
#     BALL.x += ball_speed_x
#     BALL.y += ball_speed_y
#
#     # # Проверка столкновений мяча с игроками и стенами
#     # if BALL.colliderect(PLAYER1) or BALL.colliderect(PLAYER2):
#     #     ball_speed_x *= -1
#     # if BALL.top <= 0 or BALL.bottom >= HEIGHT:
#     #     ball_speed_y *= -1
#     # if BALL.left <= 0 or BALL.right >= WIDTH:
#     #     BALL.x = WIDTH // 2 - 10
#     #     BALL.y = HEIGHT // 2 - 10
#     #     ball_speed_x *= random.choice((1, -1))
#
#     # Отскок от верхней и нижней границ
#     if BALL.top <= 0 or BALL.bottom >= HEIGHT:
#         ball_speed_y = -ball_speed_y
#
#     # Отскок от ракеток
#     if BALL.colliderect(PLAYER1):
#         ball_speed_x = -ball_speed_x
#     elif BALL.colliderect(PLAYER2):
#         ball_speed_x = -ball_speed_x
#
#     # Проверка забития гола
#     if BALL.left <= 0:
#         score_p2 += 1
#         reset_game()
#     elif BALL.right >= WIDTH:
#         score_p1 += 1
#         reset_game()
#
#
# # Функция сброса положения мяча после гола
# def reset_game():
#     global ball_speed_x, ball_speed_y, score_p1, score_p2
#     BALL.center = (WIDTH // 2, HEIGHT // 2)
#     ball_speed_x = random.choice([-4, 4])
#     ball_speed_y = random.choice([-4, 4])

# def _show_score(self):
#     score_p1, score_p2 = str(self.PLAYER1.score), str(self.PLAYER2.score)
#     score_p1 = self.font.render(score_p1, True, self.color)
#     score_p2 = self.font.render(score_p2, True, self.color)
#     self.screen.blit(score_p1, (WIDTH // 4, 50))
#     self.screen.blit(score_p2, ((WIDTH // 4) * 3, 50))


