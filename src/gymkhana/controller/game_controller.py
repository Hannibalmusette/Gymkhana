import pygame
from gymkhana.choices import choices
from gymkhana.board import Board
from gymkhana.smarter_than_you import next_move
from gymkhana.constants import WIN, BG_COLOR


class GameController:
    def __init__(self):
        self.turns_counter = 0

        # Initialize two players and allow them to choose their color, name and whether they are a bot.
        self.player_1, self.player_2 = choices()

        # Initialize the board
        self.board = Board(self.player_1.color, self.player_2.color)

        self.turn = self.player_1

    def change_turn(self):
        self.turns_counter += 1
        if self.turn == self.player_1:
            self.turn = self.player_2
        else:
            self.turn = self.player_1

    def move(self, row, col):
        if self.board.you_can_use_this_square(row, col):
            self.board.add_piece(row, col, self.turn.num, self.turn.color)
            if not self.winner():
                self.change_turn()

    def bot_turn(self) -> bool:
        return self.turn.bot

    def bot_move(self):
        self.move(*next_move(self.turns_counter, self.board, self.turn.num, self.turn.color))

    def winner(self) -> str:
        winner = self.board.winner()
        return self.turn.name if winner and not isinstance(winner, str) else winner

    def update(self, win=WIN, bg_color=BG_COLOR):
        win.fill(bg_color)
        self.board.draw(win)
        pygame.display.update()
