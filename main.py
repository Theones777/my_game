import pygame.display

from classes import *
from config import *
from funcs import create_blocks

paddle = Paddle()
ball = Ball()
blocks = create_blocks()

while True:
    sc.fill(BLACK)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Управление платформой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move(-PADDLE_SPEED)
    if keys[pygame.K_RIGHT]:
        paddle.move(PADDLE_SPEED)

    # Движение мяча
    ball.move()

    # Проверка столкновений мяча с платформой
    if ball.rect.colliderect(paddle.rect):
        ball.bounce()

    # Проверка столкновений мяча с блоками
    for block in blocks[:]:
        if ball.rect.colliderect(block.rect):
            ball.bounce()
            blocks.remove(block)

    # Проверка проигрыша
    if ball.rect.bottom >= H:
        exit()

    # Рисование объектов
    paddle.draw()
    ball.draw()
    for block in blocks:
        block.draw()

    pygame.display.update()
    clock.tick(FPS)
