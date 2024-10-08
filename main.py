import random
import pygame
from config import *

pygame.init()
sc = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption("Arcanoid")
pygame.display.set_icon(pygame.image.load("grafics/icon.bmp"))
clock = pygame.time.Clock()

x = 300
rect_color = WHITE

circle = pygame.Surface(())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif (event.type == pygame.MOUSEBUTTONDOWN and (10 < event.pos[0] < 300 and 10 < event.pos[1] < 50)):
            rect_color = random.choice([GREEN, BLUE, RED])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-= SPEED
    elif keys[pygame.K_RIGHT]:
        x += SPEED

    sc.fill(BLACK)
    pygame.draw.rect(sc, rect_color, (10, 10, 300, 50))
    pygame.draw.rect(sc, WHITE, (350, 10, 300, 50))
    pygame.draw.rect(sc, WHITE, (690, 10, 300, 50))

    pygame.draw.circle(sc, WHITE, (500, 610), 40)
    pygame.draw.line(sc, WHITE, (x, 650), (x + 400, 650), 5)
    pygame.draw.arc(sc, WHITE, (x, 500, 400, 300), 2 * pi, pi, 3)
    pygame.display.update()
    clock.tick(FPS)
