import pygame
from gymkhana.constants import SQUARE_SIZE, PADDING


class Node:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.connections = []

    def draw(self, win):
        radius = SQUARE_SIZE // 4
        pygame.draw.circle(
            win,
            self.color,
            (SQUARE_SIZE * self.col + PADDING, SQUARE_SIZE * self.row + PADDING),
            radius,
        )

    def add_connection(self, row, col):
        self.connections.append((row, col))

    def __repr__(self):
        return str(self.color) + " NODE"
