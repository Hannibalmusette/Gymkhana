import pygame
from gymkhana.constants import SQUARE_SIZE, PADDING, COLORS_DICT


class Node:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.connections = []

    def draw(self, win, sq_size=SQUARE_SIZE, padding=PADDING):
        radius = sq_size // 4
        pygame.draw.circle(
            win,
            self.color,
            (sq_size * self.col + padding, sq_size * self.row + padding),
            radius,
        )

    def add_connection(self, row: int, col: int):
        self.connections.append((row, col))

    def __repr__(self, colors_dict=COLORS_DICT):
        return colors_dict[self.color] + " NODE"
