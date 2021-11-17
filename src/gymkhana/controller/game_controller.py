import pygame
from typing import Tuple
from dataclasses import dataclass
from gymkhana.choices import choices, write_text
from gymkhana.board import Board
from gymkhana.constants.constants import SQUARE_SIZE, WHITE, WIDTH, HEIGHT
from gymkhana.smarter_than_you import next_move
from gymkhana.constants import WIN, BG_COLOR


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

    def move(self, row, col):
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
        losers = self.board.losers(self.turns_counter)
        return self.turn.name if winner else losers

    def player_and_triangle(self, win):
        i_max = HEIGHT - 50
        i_min = 490
        i_mid_min = 500
        i_mid_max = 510
        pygame.draw.polygon(
            win,
            self.player_1.color,
            ((i_mid_min, i_mid_max), (i_min, i_max), (i_mid_max, i_max)),
        )
        pygame.draw.polygon(
            win,
            self.player_2.color,
            ((i_mid_max, i_mid_min), (i_max, i_min), (i_max, i_mid_max)),
        )
        write_text("1", 490, 530, 20, 20, color=WHITE)
        write_text("2", 530, 490, 20, 20, color=WHITE, rotate=True)
        write_text(self.player_1.name, 480, 550, 30, 30, color=self.player_1.color)
        write_text(
            self.player_2.name, 550, 480, 30, 30, color=self.player_2.color, rotate=True
        )

    def update(self, win=WIN, bg_color=BG_COLOR):
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
