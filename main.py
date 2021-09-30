import pygame
from gymkhana.constants import WIDTH, HEIGHT, SQUARE_SIZE
from gymkhana.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gymkhana')

def get_square_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    if row % 2 != col % 2:
        row, col = 0, 0
    return row, col

def main():
    run = True
    game = Game(WIN)

    while run:

        if game.winner():
            print(game.winner(), 'WON')
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_square_from_mouse(pos)
                game.move(row, col)
        
        game.update()

    pygame.quit()

main()