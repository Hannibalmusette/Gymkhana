import pygame

pygame.init()

WIDTH, HEIGHT = 550, 550
ROWS, COLS = 11, 11
SQUARE_SIZE = WIDTH // COLS
FORBIDDEN_SQUARES = (
    {(x, 0) for x in range(ROWS)}
    | {(0, y) for y in range(COLS)}
    | {(x, COLS - 1) for x in range(ROWS)}
    | {(ROWS - 1, y) for y in range(COLS)}
)
PADDING = SQUARE_SIZE // 2
FONT = pygame.font.Font(None, 32)

# rgb colors
GREY = (70, 75, 80)
GREEN = (40, 65, 35)
BLUE = (40, 65, 80)
INDIGO = (55, 55, 85)
VIOLET = (70, 35, 60)
ORANGE = (85, 50, 25)

BLACK = (17, 17, 17)
WHITE = (255, 255, 255)

BG_COLOR = BLACK
WRITING_COLOR = WHITE

COLORS = [GREY, GREEN, BLUE, INDIGO, VIOLET, ORANGE]


# Pieces
PIECE_LEN = SQUARE_SIZE * 2
PIECE_LAR = SQUARE_SIZE // 3
