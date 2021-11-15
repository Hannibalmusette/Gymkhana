import random
import copy
from gymkhana.board.board import Board
from gymkhana.constants import ROWS, COLS
from gymkhana.board import Piece
from typing import List, Tuple


def get_free_squares(c_board: Board):
    return [
        (row, col)
        for (row, col) in ((row, col) for row in range(ROWS) for col in range(COLS))
        if c_board.you_can_use_this_square(row, col)
    ]
def winning_move(row: int, col: int, c_board: Board, num, color) -> bool:
    test_board = copy.deepcopy(c_board)
    test_board.add_piece(row, col, num, color)
    return test_board.winner()

def well_oriented(row: int) -> bool:
    return row % 2 != 0

def get_pieces_in_same_row(row: int, l_board: list) -> List[Piece]:
    return [
        l_board[row][c] for c in range(COLS - 1) if isinstance(l_board[row][c], Piece)
    ]

def get_pieces_in_same_col(col: int, l_board: list) -> List[Piece]:
    return [
        l_board[r][col] for r in range(ROWS - 1) if isinstance(l_board[r][col], Piece)
    ]

def blocking_continuing_nb(row: int, col: int, l_board: list) -> int:
    pieces = 0
    for piece in get_pieces_in_same_col(col, l_board):
        if piece.player_num == 1:
            pieces += 1
        else:
            pieces -= 1
    for piece in get_pieces_in_same_row(row, l_board):
        if piece.player_num == 2:
            pieces += 1
        else:
            pieces -= 1
    return pieces

def max_blocking_continuing(
    row: int, col: int, well_oriented_moves: List[Tuple], l_board: list
) -> bool:
    return blocking_continuing_nb(row, col, l_board) == max(
        [blocking_continuing_nb(r, c, l_board) for (r, c) in well_oriented_moves]
    )

def strategies(free_squares: List[Tuple], c_board: Board):
    well_oriented_moves = [(row, col) for (row, col) in free_squares if well_oriented(row)]
    l_board = c_board.board

    yield [
        (row, col)
        for (row, col) in well_oriented_moves
        if max_blocking_continuing(row, col, well_oriented_moves, l_board)
        ]
    yield well_oriented_moves if well_oriented_moves else free_squares

def next_move(turns_count, c_board, num, color) -> Tuple[int]:
    moves = []
    free_squares = get_free_squares(c_board)
        
    if turns_count >= 8:
        moves = [(row, col) for (row, col) in free_squares if winning_move(row, col, c_board, num, color)]
        if not moves:
            moves = [(row, col) for (row, col) in free_squares if winning_move(row, col, c_board, num % 2 + 1, color)]
        
    while not moves:
        moves = next(strategies(free_squares, c_board))
    move = random.choice(moves)
    return move
