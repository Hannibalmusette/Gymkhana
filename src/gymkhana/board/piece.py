import pygame
from gymkhana.constants import SQUARE_SIZE, PADDING, PIECE_LEN, PIECE_LAR


class Piece:
    def __init__(self, row, col, player, color):
        self.row = row
        self.col = col
        self.player = player
        self.color = color

    def is_horizontal(self):
        """
        Determines whether a piece has to be horizontal or vertical
        according to the player and the piece coordinates.
        :return:
        """
        return (self.player == 1 and self.row % 2 == 0) or (
            self.player == 2 and self.row % 2 != 0
        )

    def calc_size(self):
        """
        Checks if a piece is horizontal or vertical and reverses width and height if needed.
        :return: the piece's width and height
        """
        return (PIECE_LEN, PIECE_LAR) if self.is_horizontal() else (PIECE_LAR, PIECE_LEN)

    def draw(self, win):
        """
        Draws a given piece
        :param win: The screen that was defined in 'main'
        :return: nothing
        """
        width, height = self.calc_size()
        x = (SQUARE_SIZE * self.col) + PADDING - width / 2
        y = (SQUARE_SIZE * self.row) + PADDING - height / 2
        pygame.draw.rect(win, self.color, (x, y, width, height))

    def __repr__(self):
        return str(self.color) + " PIECE"
