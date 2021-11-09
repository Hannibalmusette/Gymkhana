import pygame
from .colorbox import ColorBox
from .namebox import NameBox
from .bot_or_player import TickBot
from gymkhana.constants import FONT, WIDTH, HEIGHT, WIN

pygame.init()


class InputBox:
    def __init__(self, num: int, font=FONT, win=WIN, left: int = WIDTH//18, width: int = WIDTH * 9//10, height: int = HEIGHT//4, top: int = HEIGHT//8):
        self.left = left
        self.width = width
        self.height = height
        self.top = top + self.height * (num - 1)

        self.player = "Player " + str(num) + " : "
        self.font = font

        self.color_box = ColorBox(
            win,
            self.left,
            self.top + self.height // 5,
            self.width * 2 // 3,
            self.height // 3,
        )

        self.color = self.color_box.select

        self.name_box = NameBox(
            win,
            self.left + self.width * 2 // 3,
            self.top + self.height // 4,
            self.width // 3,
            self.height // 4,
            self.color,
            self.font,
        )

        self.bot_or_player = TickBot(
            win,
            self.left + self.width * 4 // 5,
            self.top,
            self.width // 6,
            self.height // 6,
            self.color,
            self.font,
        )

    def draw(self, win=WIN, rend=True):
        """
        Draw the color box, name box, and "Player 1 :" or "Player 2 :".
        """
        self.color = self.color_box.select

        player_txt = self.font.render(self.player, rend, self.color)
        player_rect = player_txt.get_rect()
        player_rect.center = (self.left + self.width // 2, self.top)
        win.blit(player_txt, player_rect)

        self.bot_or_player.draw(win, self.color)
        self.name_box.draw(win, self.color)
        self.color_box.draw_circles()

    def handle_event(self, event):
        """
        Update choices.
        """
        return (
            self.color_box.handle_event(event),
            self.name_box.handle_event(event),
            self.bot_or_player.handle_event(event),
        )
