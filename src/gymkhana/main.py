from typing import Tuple

import pygame
from constants import MARGIN, SQUARE_SIZE
from controller import GameController


def get_square_from_mouse(pos: Tuple, sq_size=SQUARE_SIZE, margin=MARGIN) -> Tuple:
    x, y = pos
    row, col = (y - margin) // sq_size, (x - margin) // sq_size
    if row % 2 != col % 2:
        row, col = 0, 0
    return row, col


def main():
    """
    Run the game while it has to, i.e. there is no winner and no one closed the game windows.
    """
    game_controller = GameController()
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_controller.move(*get_square_from_mouse(pygame.mouse.get_pos()))

        if game_controller.winner():
            game_controller.show_winner(game_controller.winner())

        elif game_controller.bot_turn():
            game_controller.bot_move()

        pygame.display.update()
    
    pygame.quit()
    
pygame.init()
pygame.display.set_caption("Gymkhana")
main()
