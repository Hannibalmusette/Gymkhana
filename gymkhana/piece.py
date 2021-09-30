import pygame
from .constants import RED, BLUE, SQUARE_SIZE, PADDING, PIECE_LEN, PIECE_LAR

class Piece:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def is_horizontal(self):
        return (self.color == RED and self.row % 2 == 0) or (self.color == BLUE and self.row % 2 != 0) 

    def calc_size(self):
        self.width = PIECE_LEN
        self.height = PIECE_LAR
        if not self.is_horizontal():
            self.width, self.height = self.height, self.width

    def draw(self, win):
        self.calc_size()
        self.x = (SQUARE_SIZE * self.col) + PADDING - self.width / 2
        self.y = (SQUARE_SIZE * self.row) + PADDING - self.height / 2
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def __repr__(self):
        return str(self.color) + ' PIECE'