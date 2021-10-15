from gymkhana.board.piece import Piece
from gymkhana.board.node import Node
from gymkhana.constants import BG_COLOR, ROWS, COLS, FORBIDDEN_SQUARES
from typing import Generator, Tuple, List

from gymkhana.player import Player


def look_for_connections(node: Node, path: List) -> Generator:
    """
    :param node: last node reached when checking the path
    :param path: the path we are currently checking
    :return: A generator allowing to iterate on the node connections that are not already in the path
    """
    return (connection for connection in node.connections if connection not in path)


class Board:
    def __init__(self, player_1: Player, player_2: Player):
        self.board = []
        self.color_1 = player_1.color
        self.color_2 = player_2.color
        self.create(self.color_1, self.color_2)

    def create(self, color_1: Tuple, color_2: Tuple):
        """
        Creates the board as a list of list containing all the squares and what is in them.
        Since it's the beginning of the game, only nodes are added.
        All the squares that might contain pieces later get the value '0'
        :param color_1: player 1 color
        :param color_2: player 2 color
        :return: updates 'self.board' (list of list)
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
        Draws all the elements that are on the board (nodes or pieces), calling their
        respective 'draw' function.
        This function is called by the game controller after each move.
        :param win: the screen we are drawing the whole game in, defined in 'main'.
        :return: nothing
        """
        win.fill(BG_COLOR)
        for row in self.board:
            for square in row:
                if square != 0:
                    square.draw(win)

    def you_can_use_this_square(self, row: int, col: int) -> bool:
        """
        Check if it is allowed to add a piece on a given square, i.e.:
        - not a node
        - not at the end of the board
        - not occupied (value = 0)
        :return: True or False
        """
        return (
                row % 2 == col % 2
                and (row, col) not in FORBIDDEN_SQUARES
                and self.board[row][col] == 0
        )

    def connect(self, piece: Piece):
        """
        When adding a piece to the board, the two nodes that it just connected
        are updated : the other node's coordinates are added in each list of 'connections'
        :param piece: The piece that was just added to the board
        :return: nothing
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
        """
        Add a new piece to the board by adding its value in the board's list of list.
        :return: nothing
        """
        piece = Piece(row, col, num, color)
        self.board[row][col] = piece
        self.connect(piece)

    def count_empty_squares(self) -> int:
        """
        Check how many free squares are left
        """
        return (
                len([square for row in self.board for square in row if square == 0])
                - len(FORBIDDEN_SQUARES) // 2
        )

    def winning_path(self, path: List):
        """
        Checks if a given path (starting in row 0 or col 0) is winning
        (reaching the last row or col) by looking for all the connections
        between nodes and adding them in the path list.
        :return: True when the last row or col is reached, otherwise None
        """
        for connection in path:
            row, col = connection
            if row == ROWS - 1 or col == COLS - 1:
                return True
            node = self.board[row][col]
            path.extend(look_for_connections(node, path))

    def winner(self):
        """
        Checks if there is a winner but setting a path for every node that is in row 0 or col 0,
        then calling the 'winning_path' function on each of them.
        :return: True if a winning path is found, 'NO ONE' if there are no free squares left, else None
        """
        winner = None
        for row in range(ROWS):
            for col in range(COLS):
                if (col == 0 or row == 0) and isinstance(self.board[row][col], Node):
                    path = [(row, col)]
                    if self.winning_path(path):
                        winner = True
                    elif self.count_empty_squares() == 0:
                        winner = "NO ONE"

        return winner
