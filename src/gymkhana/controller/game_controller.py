import pygame
from gymkhana.player import Player
from gymkhana.inputbox import InputBox
from gymkhana.board import Board
from gymkhana.smarter_than_you import Bot
from gymkhana.constants import BG_COLOR, WRITING_COLOR, WIDTH, HEIGHT, FONT


def ready_text():
    """
    Defines the text that is displayed on the input box button (starts the game when clicked)
    :return: "READY"
    """
    text = FONT.render("READY", True, WRITING_COLOR)
    return text


def ready_rect():
    """
    Defines the size and position of the text in the "ready button"
    :return:
    """
    rect = ready_text().get_rect()
    rect.center = (WIDTH // 2, HEIGHT * 5 // 7)
    return rect


def ready_button():
    """
    Draws the 'ready button' that players click when ready.
    :return: nothing
    """
    button = pygame.Rect(
        WIDTH // 3,
        HEIGHT // 1.5,
        WIDTH // 3,
        HEIGHT // 10,
    )
    return button


def is_ready(event):
    """
    :param event: click
    :return: True when a player clicked the 'ready button'
    """
    return ready_button().collidepoint(event.pos)


class GameController:
    def __init__(self, win):
        """
        Starts the game by initializing 2 players, who each gets a random color - making sure
        they are two different colors. Then allows them to choose a color and a name
        and sets bots that can play instead of them.
        Then, it initializes the board using the two players that were defined.
        'self.tun' indicates the first player that is going to play (either player or bot).
        :param win: The screen that was defined in 'main'
        """
        self.win = win
        self.player_1 = Player(self.win, 1)
        self.player_2 = Player(self.win, 2)
        while self.player_2.color == self.player_1.color:
            self.player_2 = Player(self.win, 2)
        self.choices()

        self.board = Board(self.player_1, self.player_2)

        if self.player_1.bot:
            self.player_1 = Bot(self.player_1)

        if self.player_2.bot:
            self.player_2 = Bot(self.player_2)

        self.turn = self.player_1

    def choices(self):
        """
        Each player has a color and a name by default that were randomly defined.
        This function displays input boxes that allow them to choose, before the game actually starts.
        Each player can also be made a bot.
        It ends when a player hits the 'ready' button.
        """
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
        Draws and displays the new board.
        Has to be called after each move, as long as the game is not over.
        """
        self.board.draw(self.win)
        pygame.display.update()

    def change_turn(self):
        """
        Determines who is going to play next, according to who just did.
        """
        if self.turn == self.player_1:
            self.turn = self.player_2
        else:
            self.turn = self.player_1

    def bot_turn(self):
        """
        Checks whether the current player is a bot
        :return: True or False
        """
        return isinstance(self.turn, Bot)

    def move(self, row: int, col: int):
        """
        Checks whether the coordinates chosen by the player are a valid move.
        If it is, calls the function that adds the piece to the board.
        Then changes turn if there is no winner yet.
        """
        if self.board.you_can_use_this_square(row, col):
            self.board.add_piece(row, col, self.turn.num, self.turn.color)
            if not self.winner():
                self.change_turn()

    def bot_move(self, bot):
        """
        Calls the function that makes the bot determine its next move, and play it.
        :param bot: Either bot_1 or bot_2
        """
        row, col = bot.next_move(self.board)
        self.move(row, col)

    def winner(self):
        """
        Checks whether the board's winner function returned something, which means the game has to stop.
        :return: The winner's name ('self.turn.name'), or 'NO ONE' if the board is full.
        """
        winner = self.board.winner()
        return self.turn.name if winner and not isinstance(winner, str) else winner
