import pygame
from gymkhana.constants import SQUARE_SIZE, PADDING


class Node:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.connections = []

    def draw(self, win):
        """
        Draws a given node.
        :param win: the screen defined in 'game'
        :return: nothing
        """
        radius = SQUARE_SIZE // 4
        pygame.draw.circle(
            win,
            self.color,
            (SQUARE_SIZE * self.col + PADDING, SQUARE_SIZE * self.row + PADDING),
            radius,
        )

    def add_connection(self, row: int, col: int):
        """
        Is called each time a piece is added, on the two nodes that just got connected.
        :return: updates the 'self.connections' list for a given node.
        """
        self.connections.append((row, col))

    def __repr__(self):
        return str(self.color) + " NODE"
