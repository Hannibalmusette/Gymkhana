import pygame
from gymkhana.inputbox.colorbox import ColorBox
from gymkhana.inputbox.namebox import NameBox
from gymkhana.inputbox.bot_or_player import TickBot
from gymkhana.constants import FONT, WIDTH, HEIGHT

pygame.init()


class InputBox:
    def __init__(self, win, player: str, num: int):
        """
        Initializes the input box.
        Its position and size are calculated according to the size of the screen and the number of players.
        Initializes the color box and the name box.
        :param win: The screen that was defined in 'main'
        :param player: either "Player 1" or "Player 2"
        :param num: player's number (either 1 or 2)
        """
        self.win = win

        self.left = WIDTH // 18
        self.width = WIDTH * 9 // 10
        self.height = HEIGHT // 4

        self.top = HEIGHT // 8 + self.height * (num - 1)

        self.font = FONT

        self.color_box = ColorBox(
            self.win,
            self.left,
            self.top + self.height // 5,
            self.width * 2 // 3,
            self.height // 3,
        )

        self.color = self.color_box.select

        self.name_box = NameBox(
            self.win,
            self.left + self.width * 2 // 3,
            self.top + self.height // 4,
            self.width // 3,
            self.height // 4,
            self.color,
            self.font,
        )

        self.bot_or_player = TickBot(
            self.win,
            self.left + self.width * 4 // 5,
            self.top,
            self.width // 6,
            self.height // 6,
            self.color,
            self.font,
        )

        self.player = player

    def draw(self, win):
        """
        Draws the color box, name box, and "Player 1 :" or "Player 2 :".
        The color of the "Player" and name box is defined according to the color selected in the color box
        :param win: The screen that was defined in 'main'
        """
        self.color = self.color_box.select

        player_txt = self.font.render(self.player, True, self.color)
        player_rect = player_txt.get_rect()
        player_rect.center = (self.left + self.width // 2, self.top)
        win.blit(player_txt, player_rect)

        self.bot_or_player.draw(win, self.color)
        self.name_box.draw(win, self.color)
        self.color_box.draw_circles()

    def handle_event(self, event):
        """
        Calls the two functions that handle events in the color box and the name box respectively.
        Updates the color or name that might have been modified.
        :param event: has to be a player clicking
        :return: The chosen colors and names so far.
        """
        return (
            self.color_box.handle_event(event),
            self.name_box.handle_event(event),
            self.bot_or_player.handle_event(event),
        )
