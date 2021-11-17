import pygame
from constants import SQUARE_SIZE
from controller import GameController
from typing import Tuple


def get_square_from_mouse(pos: Tuple, sq_size=SQUARE_SIZE) -> Tuple:
    x, y = pos
    row = y // sq_size
    col = x // sq_size
    if row % 2 != col % 2:
        row, col = 0, 0
    return row, col


def main():
    """
    Run the game while it has to, i.e. there is no winner and no one closed the game windows.
    """
    run = True
    winner = False
    game_controller = GameController()

    while run:

        game_controller.update()

        if game_controller.winner():
            winner = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_controller.move(*get_square_from_mouse(pygame.mouse.get_pos()))

        if not winner and game_controller.bot_turn():
            game_controller.bot_move()

    pygame.quit()


pygame.init()
pygame.display.set_caption("Gymkhana")
main()
