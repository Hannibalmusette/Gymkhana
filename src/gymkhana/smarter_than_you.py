import random
import copy
from gymkhana.constants import ROWS, COLS
from gymkhana.board import Piece
from typing import List, Tuple


def well_oriented(row: int) -> bool:
    """
    Checks whether a piece is well oriented -i.e vertical if player 1 or horizontal if player 2-
    according to the row.
    :return: True of False
    """
    return row % 2 != 0


class Bot:
    def __init__(self, player):
        """
        Initializes a bot by giving it the name and color chosen for a player.
        :param player: The player that gets replaced by the bot.
        """
        self.player = player
        self.num = player.num
        self.color = player.color
        self.name = player.name
        self.board = None

    def scan_board(self, game_board):
        """
        Updates the 'self.board' variable by checking the current board.
        :param game_board: The list of list that represents the board
        :return: The list of list
        """
        self.board = game_board

    def pieces_in_same_row(self, row: int) -> list:
        """
        :return: A list of all the pieces that are in a given row.
        """
        return [
            self.board.board[row][c]
            for c in range(COLS - 1)
            if isinstance(self.board.board[row][c], Piece)
        ]

    def pieces_in_same_col(self, col: int) -> list:
        """
        :return: A list of all the pieces that are in a given col.
        """
        return [
            self.board.board[r][col]
            for r in range(ROWS - 1)
            if isinstance(self.board.board[r][col], Piece)
        ]

    def blocking_continuing(self, row: int, col: int) -> int:
        """
        Counts how many pieces will be either blocked or continued by playing in a given square.
        Which means they are either player 1's and in the same col, or player 2's and in the same row.
        On the other hand, if there is a player 2's piece in the same col or a player 1's piece in
        the same row, it will be one less reason to consider the move useful.
        :return: Integer
        """
        pieces = 0
        for piece in self.pieces_in_same_col(col):
            if piece.player == 1:
                pieces += 1
            else:
                pieces -= 1
        for piece in self.pieces_in_same_row(row):
            if piece.player == 2:
                pieces += 1
            else:
                pieces -= 1
        return pieces

    def winning_move(self, row: int, col: int) -> bool:
        """
        Checks whether a given move will make its player win, by making a deepcopy of the current board
        and checker whether the move will make it a winning board.
        :return: True or False
        """
        test_board = copy.deepcopy(self.board)
        if test_board.you_can_use_this_square(row, col):
            test_board.add_piece(row, col, self.num, self.color)
        return test_board.winner()

    def adversary_winning_move(self, row: int, col: int) -> bool:
        """
        Checks whether a given move will make a player's adversary win, by making a deepcopy of the current board
        and checker whether the move will make it a winning board.
        :return: True or False
        """
        num = self.num % 2 + 1
        test_board = copy.deepcopy(self.board)
        if test_board.you_can_use_this_square(row, col):
            test_board.add_piece(row, col, num, self.color)
        return test_board.winner()

    def next_move(self, game_board: List[List]) -> Tuple:
        """
        Figures out the bot next move. Tries finding the best possible move :
        Checks different strategies in a specific order (from best to worst), moving to the next,
        less specific strategy as long the list of moves returned by a strategy is empty.
        Then when a strategy gives a non-empty list of moves, randomly selects one of the moves.
        :param game_board: The current board
        """
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
