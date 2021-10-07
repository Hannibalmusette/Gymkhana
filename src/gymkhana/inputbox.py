import pygame
from gymkhana.colorbox import ColorBox
from gymkhana.namebox import NameBox
from gymkhana.constants import FONT, WRITING_COLOR

pygame.init()


class InputBox:
    def __init__(self, win, x, y, w, h, player):
        self.win = win

        self.left, self.top, self.width, self.height = x, y, w, h

        self.font = FONT

        self.color_box = ColorBox(
            self.win, self.left, self.top + self.height // 16, self.width * 2 // 3, self.height // 3
        )

        self.color = self.color_box.select

        self.name_box = NameBox(
            self.win,
            self.left + self.width * 2 // 3,
            self.top + self.height // 7,
            self.width // 3,
            self.height // 6,
            self.color,
            self.font,
        )

        self.player = player

        self.ready_button = pygame.Rect(
            self.left + self.width // 4,
            self.top + self.height // 2,
            self.width // 2,
            self.height // 6,
        )

        self.ready = "READY"
        self.ready_txt = self.font.render(self.ready, True, WRITING_COLOR)
        self.ready_rect = self.ready_txt.get_rect()
        self.ready_rect.center = (
            self.left + self.width // 2,
            self.top + self.height * 7 // 12,
        )

    def draw(self, win):
        self.color = self.color_box.select

        # Blit the player's number.
        player_txt = self.font.render(self.player, True, self.color)
        player_rect = player_txt.get_rect()
        player_rect.center = (self.left + self.width // 2, self.top)
        win.blit(player_txt, player_rect)

        self.name_box.draw(win, self.color)
        self.color_box.draw_circles()

        pygame.draw.rect(win, WRITING_COLOR, self.ready_button, 2)
        win.blit(self.ready_txt, self.ready_rect)

    def handle_event(self, event):
        return self.color_box.handle_event(event), self.name_box.handle_event(event)


    def is_ready(self, event):
        return self.ready_button.collidepoint(event.pos)
