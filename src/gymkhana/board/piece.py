from typing import Tuple

import pygame

from gymkhana.constants import (COLORS_DICT, MARGIN, PADDING, PIECE_LAR,
                                PIECE_LEN, SQUARE_SIZE, WIN)


class Piece:
    def __init__(self, row: int, col: int, num: int, color: Tuple):
        self.row = row
        self.col = col
        self.player_num = num
        self.color = color

    def is_horizontal(self) -> bool:
        return (self.player_num == 1 and self.row % 2 == 0) or (
            self.player_num == 2 and self.row % 2 != 0
        )

    def calc_size(self, le: int = PIECE_LEN, la: int = PIECE_LAR) -> Tuple:
        return (le, la) if self.is_horizontal() else (la, le)

    def calc_pos(
        self, roworcol, leorla, sq_size=SQUARE_SIZE, padding=PADDING, margin=MARGIN
    ) -> int:
        return (sq_size * roworcol) + padding - leorla / 2 + margin

    def calc_param(self):
        w, h = self.calc_size()
        x = self.calc_pos(self.col, w)
        y = self.calc_pos(self.row, h)
        return x, y, w, h

    def draw(self, win=WIN):
        pygame.draw.rect(win, self.color, self.calc_param())

    def __repr__(self, colors_dict=COLORS_DICT):
        return colors_dict[self.color] + " PIECE"
