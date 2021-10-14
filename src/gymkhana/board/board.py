from gymkhana.board.piece import Piece
from gymkhana.board.node import Node
from gymkhana.constants import BG_COLOR, ROWS, COLS, FORBIDDEN_SQUARES


def look_for_connections(node, path):
    return (connection for connection in node.connections if connection not in path)


class Board:
    def __init__(self, player_1, player_2):
        self.board = []
        self.color_1 = player_1.color
        self.color_2 = player_2.color
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
        return (
            row % 2 == col % 2
            and (row, col) not in FORBIDDEN_SQUARES
            and self.board[row][col] == 0
        )

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

    def count_empty_squares(self):
        squares = 0
        for row in self.board:
            for sq in row:
                if sq == 0:
                    squares += 1
        return squares - len(FORBIDDEN_SQUARES) // 2

    def winning_path(self, path):
        for connection in path:
            row, col = connection
            if row == ROWS - 1 or col == COLS - 1:
                return True
            node = self.board[row][col]
            path.extend(look_for_connections(node, path))

    def winner(self):
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
