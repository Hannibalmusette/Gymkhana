import pygame
from gymkhana.player import Player
from gymkhana.inputbox import InputBox
from gymkhana.board import Board
from gymkhana.smarter_than_you import Bot
from gymkhana.constants import BG_COLOR, WRITING_COLOR, WIDTH, HEIGHT, FONT


def ready_text():
    text = FONT.render("READY", True, WRITING_COLOR)
    return text


def ready_rect():
    rect = ready_text().get_rect()
    rect.center = (WIDTH // 2, HEIGHT * 5 // 7)
    return rect


def ready_button():
    button = pygame.Rect(
        WIDTH // 3,
        HEIGHT // 1.5,
        WIDTH // 3,
        HEIGHT // 10,
    )
    return button


def is_ready(event):
    return ready_button().collidepoint(event.pos)


class GameController:
    def __init__(self, win):
        self.win = win
        self.player_1 = Player(self.win, 1)
        self.player_2 = Player(self.win, 2)
        self.choices()

        self.board = Board(self.player_1, self.player_2)
        self.turn = self.player_1
        self.bot = Bot(self.board, self.player_2)

    def choices(self):
        input_box_1 = InputBox(self.win, self.player_1.player, 1)
        input_box_2 = InputBox(self.win, self.player_2.player, 2)

        done = False

        while not done:

            self.win.fill(BG_COLOR)

            input_box_1.draw(self.win)
            input_box_2.draw(self.win)

            pygame.draw.rect(self.win, WRITING_COLOR, ready_button(), 2)
            self.win.blit(ready_text(), ready_rect())

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif (
                        event.type == pygame.MOUSEBUTTONDOWN
                        and is_ready(event)
                        and self.player_1.color != self.player_2.color
                ):
                    done = True
                else:
                    self.player_1.color, self.player_1.name = input_box_1.handle_event(
                        event
                    )
                    self.player_2.color, self.player_2.name = input_box_2.handle_event(
                        event
                    )

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def change_turn(self):
        if self.turn == self.player_1:
            self.turn = self.bot
        else:
            self.turn = self.player_1

    def move(self, row, col):
        if self.board.you_can_use_this_square(row, col):
            self.board.add_piece(row, col, self.turn.num, self.turn.color)
            if not self.winner():
                self.change_turn()
                if self.turn == self.bot:
                    row, col = self.bot.next_move(self.board)
                    self.move(row, col)

    def winner(self):
        winner = self.board.winner()
        return self.turn.name if winner and not isinstance(winner, str) else winner
