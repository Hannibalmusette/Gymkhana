import pygame
from gymkhana.constants import WIDTH, HEIGHT, SQUARE_SIZE
from gymkhana.controller import GameController
from typing import Tuple

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gymkhana")


def get_square_from_mouse(pos: Tuple) -> Tuple:
    """
    :param pos: mouse position (x, y)
    :return: the square in which the mouse is positioned (row, col)
    """
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    if row % 2 != col % 2:
        row, col = 0, 0
    return row, col


def main():
    """
    Runs the game while it has to, i.e. there is no winner and no one closed the game windows.
    Updates the game constantly.
    If there is a bot, calls it when it has to play.
    Stops the game if there is a winner and prints which player it is.
    """
    run = True
    game_controller = GameController(WIN)

    while run:

        if game_controller.winner():
            print(game_controller.winner(), "WON")
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_square_from_mouse(pos)
                game_controller.move(row, col)

        if (
            game_controller.turn == game_controller.bot_1
            or game_controller.turn == game_controller.bot_2
        ):
            bot = game_controller.turn
            game_controller.bot_move(bot)

        game_controller.update()

    pygame.quit()


main()
