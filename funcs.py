from classes import Block
from config import *


def create_blocks():
    blocks = []
    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLUMNS):
            block = Block(col * BLOCK_WIDTH, row * BLOCK_HEIGHT)
            blocks.append(block)
    return blocks
