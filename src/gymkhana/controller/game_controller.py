from dataclasses import dataclass
from typing import Tuple

import pygame

from gymkhana.board import Board, player_and_triangle
from gymkhana.choices import choices, write_text
from gymkhana.constants import BG_COLOR, WIN
from gymkhana.constants.constants import HEIGHT, SQUARE_SIZE, WIDTH
from gymkhana.smarter_than_you import next_move


@dataclass
class Player:
    num: int
    color: Tuple
    name: str
    bot: bool


class GameController:
    def __init__(self):
        self.turns_counter = 0

        # Allow the two players to choose their color, name and whether they are a bot.
        player_1, player_2 = choices()
        self.player_1 = Player(1, *player_1)
        self.player_2 = Player(2, *player_2)

        # Initialize the board
        self.board = Board(self.player_1.color, self.player_2.color)
        player_and_triangle(self.player_1, self.player_2)

        self.turn = self.player_1

    def change_turn(self):
        self.turns_counter += 1
        if self.turn == self.player_1:
            self.turn = self.player_2
        else:
            self.turn = self.player_1

    def move(self, row: int, col: int):
        if self.board.you_can_use_this_square(row, col):
            self.board.draw_piece(
                self.board.add_piece(row, col, self.turn.num, self.turn.color)
            )
            if not self.winner():
                self.change_turn()

    def bot_turn(self) -> bool:
        return self.turn.bot

    def bot_move(self):
        self.move(
            *next_move(self.turns_counter, self.board, self.turn.num, self.turn.color)
        )

    def winner(self) -> str:
        winner = self.board.winner()
        return self.turn.name if winner else self.board.losers(self.turns_counter)

    def show_winner(
        self, winner: str, win: pygame.Surface = WIN, bg_color: Tuple = BG_COLOR
    ):
        win.fill(bg_color)
        winner_txt = winner + " WON !"
        write_text(
            winner_txt,
            WIDTH // 3,
            HEIGHT // 3,
            WIDTH // 3,
            HEIGHT // 4,
            color=self.turn.color,
        )
