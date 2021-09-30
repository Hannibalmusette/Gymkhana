import pygame
from .constants import (
    RED,
    BLUE,
    SQUARE_SIZE,
    PADDING
)

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = RED if row % 2 == 0 else BLUE
        self.connections = []

    def draw(self, win):
        radius = SQUARE_SIZE // 4
        pygame.draw.circle(
            win,
            self.color,
            #we need the coordinates
            (SQUARE_SIZE * self.col + PADDING, SQUARE_SIZE * self.row + PADDING),
            radius
        )

    def add_connection(self, row, col):
        self.connections.append((row, col))

    def __repr__(self):
        return str(self.color) + ' NODE'