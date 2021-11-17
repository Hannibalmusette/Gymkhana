from dataclasses import dataclass
from typing import Tuple

import pygame

from gymkhana.board import Board
from gymkhana.choices import choices, write_text
from gymkhana.constants import BG_COLOR, WIN
from gymkhana.constants.constants import (HEIGHT, MARGIN, SQUARE_SIZE, WHITE,
                                          WIDTH)
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

        self.turn = self.player_1

    def change_turn(self):
        self.turns_counter += 1
        if self.turn == self.player_1:
            self.turn = self.player_2
        else:
            self.turn = self.player_1

    def move(self, row: int, col: int):
        if self.board.you_can_use_this_square(row, col):
            self.board.add_piece(row, col, self.turn.num, self.turn.color)
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

    def player_and_triangle(self, win, margin=MARGIN):
        som_j = margin * 1.8
        som_i = margin * 2
        bas_j = margin
        bas_i_1 = som_j
        bas_i_2 = margin * 2.2
        pygame.draw.polygon(
            win,
            self.player_1.color,
            ((bas_i_1, bas_j), (bas_i_2, bas_j), (som_i, som_j)),
        )
        pygame.draw.polygon(
            win,
            self.player_2.color,
            ((bas_j, bas_i_1), (bas_j, bas_i_2), (som_j, som_i)),
        )
        write_text("1", som_j, bas_j, margin // 2.5, margin // 2.5, color=WHITE)
        write_text(
            "2", bas_j, som_j, margin // 2.5, margin // 2.5, color=WHITE, rotate=True
        )
        write_text(
            self.player_1.name,
            bas_i_2,
            margin // 3,
            margin // 1.5,
            margin // 1.5,
            color=self.player_1.color,
        )
        write_text(
            self.player_2.name,
            margin // 3,
            bas_i_2,
            30,
            30,
            color=self.player_2.color,
            rotate=True,
        )

    def update(self, win: pygame.Surface = WIN, bg_color: Tuple = BG_COLOR):
        win.fill(bg_color)
        if self.winner():
            winner_txt = self.winner() + " WON !"
            write_text(
                winner_txt, WIDTH // 3, HEIGHT // 3, SQUARE_SIZE * 4, SQUARE_SIZE * 2
            )
        else:
            self.player_and_triangle(win)
            self.board.draw(win)
        pygame.display.update()
