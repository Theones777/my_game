import pygame

FPS = 60
W, H = 1000, 700

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pi = 3.14
SPEED = 25


# Параметры платформы
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 10

# Параметры мяча
BALL_SIZE = 20
BALL_SPEED = [4, -4]

# Параметры блоков
BLOCK_ROWS = 5
BLOCK_COLUMNS = 8
BLOCK_WIDTH = W // BLOCK_COLUMNS
BLOCK_HEIGHT = 30


pygame.init()
sc = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption("Arcanoid")
pygame.display.set_icon(pygame.image.load("grafics/icon.bmp"))
clock = pygame.time.Clock()