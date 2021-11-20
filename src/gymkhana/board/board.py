from typing import Generator, List, Tuple

from pygame import Surface

from gymkhana.board.node import Node
from gymkhana.board.piece import Piece
from gymkhana.constants import BG_COLOR, COLS, FORBIDDEN_SQUARES, ROWS, WIN


def look_for_connections(node: Node, path: List) -> Generator:
    return (connection for connection in node.connections if connection not in path)


class Board:
    def __init__(self, color_1: Tuple, color_2: Tuple):
        self.board = []
        self.color_1 = color_1
        self.color_2 = color_2
        self.initial_board()
        self.init_free_squares = (
            len([square for row in self.board for square in row])
            - len(FORBIDDEN_SQUARES)
        ) // 2 + 1

    def initial_board(self, win=WIN, bg_color=BG_COLOR):
        win.fill(bg_color)
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row % 2 == col % 2:
                    self.board[row].append(0)
                else:
                    node = (
                        Node(row, col, self.color_1)
                        if row % 2 == 0
                        else Node(row, col, self.color_2)
                    )
                    self.board[row].append(node)
                    node.draw()

    def you_can_use_this_square(self, row: int, col: int) -> bool:
        """
        Check if it is allowed to add a piece on a given square.
        """
        return (
            row % 2 == col % 2
            and (row, col) not in FORBIDDEN_SQUARES
            and self.board[row][col] == 0
        )

    def connect(self, piece: Piece):
        """
        Add each of the two nodes that were connected to the other one's list of connections
        """
        row = piece.row
        col = piece.col
        if piece.is_horizontal():
            node_1 = self.board[row][col - 1]
            node_2 = self.board[row][col + 1]
        else:
            node_1 = self.board[row - 1][col]
            node_2 = self.board[row + 1][col]
        node_1.add_connection(node_2.row, node_2.col)
        node_2.add_connection(node_1.row, node_1.col)

    def add_piece(self, row: int, col: int, num: int, color: Tuple):
        piece = Piece(row, col, num, color)
        self.board[row][col] = piece
        self.connect(piece)
        return piece

    def draw_piece(self, piece: Piece):
        piece.draw()

    def winning_path(self, path: List):
        """
        Check if a given path is winning.
        """
        for connection in path:
            row, col = connection
            if row == ROWS - 1 or col == COLS - 1:
                return True
            node = self.board[row][col]
            path.extend(look_for_connections(node, path))

    def winner(self):
        """
        Check if there is a winner.
        """
        winner = None
        for row in range(ROWS):
            for col in range(COLS):
                if (col == 0 or row == 0) and isinstance(self.board[row][col], Node):
                    path = [(row, col)]
                    if self.winning_path(path):
                        winner = True
                        break
        return winner

    def losers(self, turns_count):
        if self.init_free_squares - turns_count == 0:
            return "NO ONE"
