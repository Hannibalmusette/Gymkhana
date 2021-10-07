from gymkhana.board.piece import Piece
from gymkhana.board.node import Node
from gymkhana.constants import BG_COLOR, ROWS, COLS, FORBIDDEN_SQUARES


class Board:
    def __init__(self, color_1, color_2):
        self.board = []
        self.color_1 = color_1
        self.color_2 = color_2
        self.create(self.color_1, self.color_2)

    def create(self, color_1, color_2):
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
        win.fill(BG_COLOR)
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
            node_1 = self.board[row][col - 1]
            node_2 = self.board[row][col + 1]
        else:
            node_1 = self.board[row - 1][col]
            node_2 = self.board[row + 1][col]
        node_1.add_connection(node_2.row, node_2.col)
        node_2.add_connection(node_1.row, node_1.col)

    def add_piece(self, row, col, num, color):
        piece = Piece(row, col, num, color)
        self.board[row][col] = piece
        self.connect(piece)

    def look_for_connections(self, node, path):
        return (connection for connection in node.connections if connection not in path)

    def winning_path(self, node, path):
        for connection in self.look_for_connections(node, path):
            path.append(connection)
            row, col = connection
            return (
                self.winning_path(self.board[row][col], path)
                if max(col, row) < 10
                else "END"
            )

    def winner(self):
        winner = None
        for row in range(ROWS):
            for col in range(COLS):
                if (col == 0 or row == 0) and isinstance(self.board[row][col], Node):
                    departure_node = self.board[row][col]
                    path = [(row, col)]
                    if self.winning_path(departure_node, path):
                        winner = "ok"

        return winner
