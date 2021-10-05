import pygame
from .player import Player
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.player_1 = Player(1)
        self.player_2 = Player(2)
        self.board = Board(self.player_1.color, self.player_2.color)
        self.turn = self.player_1

    def reset(self):
        self._init()

    def change_turn(self):
        if self.turn == self.player_1:
            self.turn = self.player_2
        else:
            self.turn = self.player_1

    def move(self, row, col):
        if self.board.you_can_use_this_square(row, col):
            self.board.add_piece(row, col, self.turn.num, self.turn.color)
            if not self.winner():
                self.change_turn()

    def winner(self):
        return self.turn.name if self.board.winner() else None