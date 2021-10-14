import pygame
from gymkhana.colorbox import ColorBox
from gymkhana.namebox import NameBox
from gymkhana.constants import FONT, WRITING_COLOR, WIDTH, HEIGHT

pygame.init()


class InputBox:
    def __init__(self, win, player, num):
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

        self.player = player

    def draw(self, win):
        self.color = self.color_box.select

        # Blit the player's number.
        player_txt = self.font.render(self.player, True, self.color)
        player_rect = player_txt.get_rect()
        player_rect.center = (self.left + self.width // 2, self.top)
        win.blit(player_txt, player_rect)

        self.name_box.draw(win, self.color)
        self.color_box.draw_circles()

    def handle_event(self, event):
        return self.color_box.handle_event(event), self.name_box.handle_event(event)
