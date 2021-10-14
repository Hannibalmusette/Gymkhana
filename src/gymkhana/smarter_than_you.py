import random
import copy
from gymkhana.constants import ROWS, COLS
from gymkhana.board import Piece, Board


def well_oriented(row):
    return row % 2 != 0


class Bot:
    def __init__(self, game_board, player):
        self.num = player.num
        self.color = player.color
        self.name = player.name
        self.board = game_board

    def scan_board(self, game_board):
        self.board = game_board

    def pieces_in_same_row(self, row):
        pieces = 0
        for c in range(COLS-1):
            elem = self.board.board[row][c]
            if isinstance(elem, Piece):
                pieces += 1
        return pieces

    def pieces_in_same_col(self, col):
        pieces = 0
        for r in range(ROWS-1):
            elem = self.board.board[r][col]
            if isinstance(elem, Piece):
                pieces += 1
        return pieces

    def winning_move(self, row, col):
        test_board = copy.deepcopy(self.board)
        if test_board.you_can_use_this_square(row, col):
            test_board.add_piece(row, col, self.num, self.color)
        return test_board.winner()

    def next_move(self, game_board):
        self.scan_board(game_board)
        all_squares = ((row, col) for row in range(ROWS) for col in range(COLS))
        free_squares = [(row, col) for (row, col) in all_squares if self.board.you_can_use_this_square(row, col)]
        well_oriented_moves = [(row, col) for (row, col) in free_squares if well_oriented(row)]
        winning_moves = [(row, col) for (row, col) in free_squares if self.winning_move(row, col)]
        moves = winning_moves
        if not moves:
            moves = [(row, col) for (row, col) in well_oriented_moves if self.pieces_in_same_row(row) or self.pieces_in_same_col(col)]
            if not moves:
                moves = well_oriented_moves if well_oriented_moves else free_squares
        move = moves[random.randint(0, len(moves) - 1)] if len(moves) > 1 else moves[0]
        return move
