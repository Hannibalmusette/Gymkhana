import pygame
from .colorbox import ColorBox
from .namebox import NameBox
from .bot_or_player import TickBot
from .write_text import write_text
from gymkhana.constants import WIDTH, HEIGHT, WIN

pygame.init()


class InputBox:
    def __init__(
        self,
        num: int,
        x: int = WIDTH // 18,
        y: int = HEIGHT // 8,
        w: int = WIDTH * 9 // 10,
        h: int = HEIGHT // 4,
        
    ):
        self.num = num
        self.left = x
        self.top = y + h * (self.num - 1)
        self.width = w
        self.height = h
        
        self.name_box = NameBox(
            self.left + self.width * 2 // 3,
            self.top + self.height // 4,
            self.width // 3,
            self.height // 4,
        )

        self.bot_or_player = TickBot(
            self.left + self.width * 4 // 5,
            self.top,
            self.width // 5,
            self.height // 6,
        )

        self.color_box = ColorBox(
            self.left,
            self.top + self.height // 5,
            self.width * 2 // 3,
            self.height // 3,
        )

        self.color = self.color_box.select

    def draw(self, win=WIN):
        """
        Draw the color box, name box, and "Player 1 :" or "Player 2 :".
        """
        self.color = self.color_box.select

        player_txt = "Player " + str(self.num) + " : "
        write_text(player_txt, self.left, self.top, self.width, 0, color=self.color)

        self.bot_or_player.draw(win, self.color)
        self.name_box.draw(win, self.color)
        self.color_box.draw_circles()

    def handle_event(self, event):
        self.color_box.handle_event(event)
        self.name_box.handle_event(event)
        self.bot_or_player.handle_event(event)
        return self.color_box.select, self.name_box.text, self.bot_or_player.bot
