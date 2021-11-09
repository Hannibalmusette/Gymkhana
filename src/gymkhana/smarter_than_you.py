import random
import copy
from gymkhana.constants import ROWS, COLS, TOTAL_SQUARES
from gymkhana.board import Piece
from typing import List, Tuple

def well_oriented(row: int) -> bool:
    """
    Check whether a piece is well oriented -i.e vertical if player 1 or horizontal if player 2-
    according to the row.
    """
    return row % 2 != 0

def get_free_squares(c_board):
    return[(row, col) for (row, col) in ((row, col) for row in range(ROWS) for col in range(COLS)) if c_board.you_can_use_this_square(row, col)]

def get_pieces_in_same_row(row: int, l_board: list) -> list:
    return [l_board[row][c] for c in range(COLS - 1) if isinstance(l_board[row][c], Piece)]

def get_pieces_in_same_col(col: int, l_board: list) -> list:
    return [l_board[r][col] for r in range(ROWS - 1) if isinstance(l_board[r][col], Piece)]

def blocking_continuing_nb(row: int, col: int, l_board: list) -> int:
    pieces = 0
    for piece in get_pieces_in_same_col(col, l_board):
        if piece.player == 1:
            pieces += 1
        else:
            pieces -= 1
    for piece in get_pieces_in_same_row(row, l_board):
        if piece.player == 2:
            pieces += 1
        else:
            pieces -= 1
    return pieces

class Bot:
    def __init__(self, player):
        self.player = player
        self.num = player.num
        self.color = player.color
        self.name = player.name

    def max_blocking_continuing(
        self, row: int, col: int, well_oriented_moves: List[Tuple], l_board: list
    ) -> bool:
        return blocking_continuing_nb(row, col, l_board) == max(
            [blocking_continuing_nb(r, c, l_board) for (r, c) in well_oriented_moves]
        )

    def winning_move(self, row: int, col: int, c_board) -> bool:
        test_board = copy.deepcopy(c_board)
        test_board.add_piece(row, col, self.num, self.color)
        return test_board.winner()

    def adversary_winning_move(self, row: int, col: int, c_board) -> bool:
        """
        Checks whether a given move will make a player's adversary win.
        """
        num = self.num % 2 + 1
        test_board = copy.deepcopy(c_board)
        if test_board.you_can_use_this_square(row, col):
            test_board.add_piece(row, col, num, self.color)
        return test_board.winner()

    def next_move(self, c_board, turns_count) -> Tuple:
        """
        Figure out the bot next move : try to find the best possible move by checking different strategies in a specific order.
        """
        moves = []
        l_board = c_board.board
        free_squares = get_free_squares(c_board)

        if turns_count >= 8:

            moves = [
                (row, col)
                for (row, col) in free_squares
                if self.winning_move(row, col, c_board)
            ]

            if not moves:
                moves = [
                    (row, col)
                    for (row, col) in free_squares
                    if self.adversary_winning_move(row, col, c_board)
                ]

        if not moves:
            well_oriented_moves = [
                (row, col) for (row, col) in free_squares if well_oriented(row)
            ]

            moves = [
                (row, col)
                for (row, col) in well_oriented_moves
                if self.max_blocking_continuing(row, col, well_oriented_moves, l_board)
            ]

            if not moves:
                moves = [
                    (row, col)
                    for (row, col) in well_oriented_moves
                    if blocking_continuing_nb(row, col, l_board)
                ]
            if not moves:
                moves = [
                    well_oriented_moves if well_oriented_moves else free_squares
                ]

        move = moves[random.randint(0, len(moves) - 1)] if len(moves) > 1 else moves[0]

        return move
