from config import *


class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(W // 2 - PADDLE_WIDTH // 2, H - 50, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > W:
            self.rect.right = W

    def draw(self):
        pygame.draw.rect(sc, WHITE, self.rect)


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(W // 2, H // 2, BALL_SIZE, BALL_SIZE)
        self.speed = BALL_SPEED.copy()

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        # Отражение от стен
        if self.rect.left <= 0 or self.rect.right >= W:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]

    def bounce(self):
        self.speed[1] = -self.speed[1]

    def draw(self):
        pygame.draw.ellipse(sc, BLUE, self.rect)


class Block:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)

    def draw(self):
        pygame.draw.rect(sc, RED, self.rect)