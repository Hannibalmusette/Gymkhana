import pygame
from .constants import RED, BLUE
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.board = Board()
        self.turn = RED

    def reset(self):
        self._init()

    def change_turn(self):
        if self.turn == RED:
            self.turn = BLUE
        else:
            self.turn = RED

    def move(self, row, col):
        if self.board.you_can_use_this_square(row, col):
            self.board.add_piece(row, col, self.turn)
            if not self.winner():
                self.change_turn()

    def winner(self):
        return self.turn if self.board.winner() else None