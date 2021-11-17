import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
MARGIN = WIDTH // 12
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
ROWS, COLS = 11, 11
SQUARE_SIZE = (WIDTH - MARGIN) // COLS
FORBIDDEN_SQUARES = (
    {(x, 0) for x in range(ROWS)}
    | {(0, y) for y in range(COLS)}
    | {(x, COLS - 1) for x in range(ROWS)}
    | {(ROWS - 1, y) for y in range(COLS)}
)
TOTAL_SQUARES = ROWS * COLS - 2 * len(FORBIDDEN_SQUARES)
PADDING = SQUARE_SIZE // 2
FONT = pygame.font.Font(None, 32)

BLACK = (17, 17, 17)
WHITE = (255, 255, 255)

BG_COLOR = BLACK
WRITING_COLOR = WHITE

PIECE_LEN = SQUARE_SIZE * 2
PIECE_LAR = SQUARE_SIZE // 3
