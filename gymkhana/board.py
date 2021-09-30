from .piece import Piece
from .node import Node
from .constants import BGCOLOR, ROWS, COLS, FORBIDDEN_SQUARES

class Board:
    def __init__(self):
        self.board = []
        self.create()

    def create(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row % 2 == col % 2:
                    self.board[row].append(0)
                else:
                    self.board[row].append(Node(row, col))

    def draw(self, win):
        win.fill(BGCOLOR)
        for row in self.board:
            for sq in row:
                elem = sq
                if elem != 0:
                    elem.draw(win)

    def you_can_use_this_square(self, row, col):
        return (row, col) not in FORBIDDEN_SQUARES and self.board[row][col] == 0

    def connect(self, piece):
        row = piece.row
        col = piece.col
        if piece.is_horizontal():
            node_1 = self.board[row][col-1]
            node_2 = self.board[row][col+1]
        else:
            node_1 = self.board[row-1][col]
            node_2 = self.board[row+1][col]
        node_1.add_connection(node_2.row, node_2.col)
        node_2.add_connection(node_1.row, node_1.col)

    def add_piece(self, row, col, color):
        piece = Piece(row, col, color)
        self.board[row][col] = piece
        self.connect(piece)

    def look_for_connections(self, node, path):
        return (connection for connection in node.connections if connection not in path)

    def winning_path(self, node, path):
        for connection in self.look_for_connections(node, path):
            path.append(connection)
            row, col = connection
            return self.winning_path(self.board[row][col], path) if col < 10 and row < 10 else 'END'

    def winner(self):
        winner = None
        for row in range(ROWS):
            for col in range(COLS):
                if (col == 0 or row == 0) and isinstance(self.board[row][col], Node):
                    departure_node = self.board[row][col]
                    path = [(row, col)]
                    if self.winning_path(departure_node, path):
                        winner = 'yes'

        return winner
