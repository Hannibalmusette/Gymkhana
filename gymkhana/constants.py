import random

WIDTH, HEIGHT = 550, 550
ROWS, COLS = 11, 11
SQUARE_SIZE = WIDTH // COLS
FORBIDDEN_SQUARES = {(x, 0) for x in range(ROWS)} | {(0, y) for y in range(COLS)} | {(x, COLS-1) for x in range(ROWS)} | {(ROWS-1, y) for y in range(COLS)}
PADDING = SQUARE_SIZE // 2

#rgb colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (15, 85, 100)
GREY = (126, 126, 126)
BLACK = (0, 0, 0)
VIOLET = (50, 5, 50)
YELLOW = (85, 85, 25)
WHITE = (255, 255, 255)

COLORS = [RED, GREEN, BLUE, CYAN, GREY, BLACK, VIOLET, YELLOW, WHITE]
BGCOLOR = COLORS.pop(random.randint(0, len(COLORS)-1))

# Pieces 
PIECE_LEN = SQUARE_SIZE * 2
PIECE_LAR = SQUARE_SIZE // 3