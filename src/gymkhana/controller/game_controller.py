import pygame
from gymkhana.player import Player
from gymkhana.inputbox import InputBox
from gymkhana.board import Board
from gymkhana.smarter_than_you import Bot
from gymkhana.constants import BG_COLOR, WRITING_COLOR, WIDTH, HEIGHT, FONT
from typing import Tuple


def ready_rect(txt : str = "READY", font=FONT, rend=True, color=WRITING_COLOR, width=WIDTH, height=HEIGHT):
    text = font.render(txt, rend, color)
    rect = text.get_rect()
    rect.center = (width // 2, height * 5 // 7)
    return text, rect


def ready_button(x=WIDTH//3, y=HEIGHT//1.5, l=WIDTH//3, h=HEIGHT//10):
    return pygame.Rect(x, y, l, h)


def is_ready(event) -> bool:
    return event.type == pygame.MOUSEBUTTONDOWN and ready_button().collidepoint(event.pos)


class GameController:
    def __init__(self, win):
        self.win = win

        #Initialize two players who each gets a random color
        self.player_1 = Player(self.win, 1)
        self.player_2 = Player(self.win, 2)

        # Make sure each player gets a different color
        while self.player_2.color == self.player_1.color:
            self.player_2 = Player(self.win, 2)

        # Allow the players to choose their color, name and whether they are a bot.
        self.choices()

        #Initialize the board
        self.board = Board(self.player_1, self.player_2)

        if self.player_1.bot:
            self.player_1 = Bot(self.player_1)
        if self.player_2.bot:
            self.player_2 = Bot(self.player_2)

        self.turn = self.player_1

    def choices(self, bgcolor=BG_COLOR, color=WRITING_COLOR):
        """
        Display input boxes that allow the players to choose their name and color.
        Each player can also be made a bot.
        """
        input_box_1 = InputBox(self.win, self.player_1.player, 1)
        input_box_2 = InputBox(self.win, self.player_2.player, 2)

        done = False

        while not done:

            self.win.fill(bgcolor)

            input_box_1.draw(self.win)
            input_box_2.draw(self.win)

            pygame.draw.rect(self.win, color, ready_button(), 2)
            self.win.blit(*ready_rect())

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif (
                    is_ready(event)
                    and self.player_1.color != self.player_2.color
                ):
                    done = True
                else:
                    (
                        self.player_1.color,
                        self.player_1.name,
                        self.player_1.bot,
                    ) = input_box_1.handle_event(event)
                    (
                        self.player_2.color,
                        self.player_2.name,
                        self.player_2.bot,
                    ) = input_box_2.handle_event(event)

    def update(self):
        """
        Draw and display the board after each move.
        """
        self.board.draw(self.win)
        pygame.display.update()

    def change_turn(self):
        if self.turn == self.player_1:
            self.turn = self.player_2
        else:
            self.turn = self.player_1

    def bot_turn(self) -> bool:
        """
        Check whether the current player is a bot
        """
        return isinstance(self.turn, Bot)

    def move(self, row, col):
        if self.board.you_can_use_this_square(row, col):
            self.board.add_piece(row, col, self.turn.num, self.turn.color)
            if not self.winner():
                self.change_turn()

    def bot_move(self, bot: Bot):
        """
        Call and play a bot's next move.
        """
        row, col = bot.next_move(self.board)
        self.move(row, col)

    def winner(self) -> str:
        """
        Check whether someone won.
        Return the winner's name ('self.turn.name'), or 'NO ONE' if the board is full.
        """
        winner = self.board.winner()
        return self.turn.name if winner and not isinstance(winner, str) else winner
