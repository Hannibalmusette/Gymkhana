import pygame
from gymkhana.constants import SQUARE_SIZE
from gymkhana.controller import GameController
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
    game_controller = GameController()

    while run:

        if game_controller.winner():
            print(game_controller.winner(), "WON")
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_controller.move(*get_square_from_mouse(pygame.mouse.get_pos()))

        if game_controller.bot_turn():
            game_controller.bot_move(game_controller.turn)

        game_controller.update()

    pygame.quit()

pygame.init()
pygame.display.set_caption("Gymkhana")
main()
