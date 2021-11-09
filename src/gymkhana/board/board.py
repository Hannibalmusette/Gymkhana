from gymkhana.board.piece import Piece
from gymkhana.board.node import Node
from gymkhana.constants import BG_COLOR, ROWS, COLS, FORBIDDEN_SQUARES
from typing import Generator, Tuple, List

from gymkhana.player import Player


def look_for_connections(node: Node, path: List) -> Generator:
    """
    For a given node, look for connections that are not in its path.
    """
    return (connection for connection in node.connections if connection not in path)


class Board:
    def __init__(self, player_1: Player, player_2: Player):
        self.board = []
        self.color_1 = player_1.color
        self.color_2 = player_2.color
        self.initial_board(self.color_1, self.color_2)

    def initial_board(self, color_1: Tuple, color_2: Tuple):
        """
        Create the board as a list of list containing all the squares and what is in them.
        Since it is the beginning of the game, only nodes are added.
        All the squares that might contain pieces later get the value '0'
        """
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row % 2 == col % 2:
                    self.board[row].append(0)
                else:
                    if row % 2 == 0:
                        color = color_1
                    else:
                        color = color_2
                    self.board[row].append(Node(row, col, color))

    def draw(self, win):
        """
        Draw all the elements (node or piece) that are on the board.
        """
        win.fill(BG_COLOR)
        for row in self.board:
            for square in row:
                if square != 0:
                    square.draw(win)

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

    def add_piece(self, row, col, num: int, color: Tuple):
        piece = Piece(row, col, num, color)
        self.board[row][col] = piece
        self.connect(piece)

    def count_empty_squares(self) -> int:
        """
        Check how many free squares are left.
        """
        return (
            len([square for row in self.board for square in row if square == 0])
            - len(FORBIDDEN_SQUARES) // 2
        )

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
                    if self.count_empty_squares() == 0:
                        winner = "NO ONE"
                        break
                    elif self.winning_path(path):
                        winner = True
                        break
        return winner
