import random
import copy
from gymkhana.constants import ROWS, COLS
from gymkhana.board import Piece


def well_oriented(row):
    return row % 2 != 0


class Bot:
    def __init__(self, player):
        self.num = player.num
        self.color = player.color
        self.name = player.name
        self.board = None

    def scan_board(self, game_board):
        self.board = game_board

    def pieces_in_same_row(self, row):
        return [
            self.board.board[row][c]
            for c in range(COLS - 1)
            if isinstance(self.board.board[row][c], Piece)
        ]

    def pieces_in_same_col(self, col):
        return [
            self.board.board[r][col]
            for r in range(ROWS - 1)
            if isinstance(self.board.board[r][col], Piece)
        ]

    def blocking_continuing(self, row, col):
        pieces = 0
        for piece in self.pieces_in_same_col(col):
            if piece.player == 1:
                pieces += 1
        for piece in self.pieces_in_same_row(row):
            if piece.player == 2:
                pieces += 1
        return pieces

    def winning_move(self, row, col):
        test_board = copy.deepcopy(self.board)
        if test_board.you_can_use_this_square(row, col):
            test_board.add_piece(row, col, self.num, self.color)
        return test_board.winner()

    def adversary_winning_move(self, row, col):
        num = self.num % 2 + 1
        test_board = copy.deepcopy(self.board)
        if test_board.you_can_use_this_square(row, col):
            test_board.add_piece(row, col, num, self.color)
        return test_board.winner()

    def next_move(self, game_board):
        self.scan_board(game_board)

        free_squares = [
            (row, col)
            for (row, col) in ((row, col) for row in range(ROWS) for col in range(COLS))
            if self.board.you_can_use_this_square(row, col)
        ]

        moves = [
            (row, col) for (row, col) in free_squares if self.winning_move(row, col)
        ]

        if not moves:
            moves = [
                (row, col)
                for (row, col) in free_squares
                if self.adversary_winning_move(row, col)
            ]

        if not moves:
            well_oriented_moves = [
                (row, col) for (row, col) in free_squares if well_oriented(row)
            ]
            moves = [
                (row, col)
                for (row, col) in well_oriented_moves
                if self.blocking_continuing(row, col)
            ]
            if not moves:
                moves = well_oriented_moves if well_oriented_moves else free_squares

        move = moves[random.randint(0, len(moves) - 1)] if len(moves) > 1 else moves[0]

        return move
