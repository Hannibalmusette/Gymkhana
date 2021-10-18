import pygame
from gymkhana.constants import WRITING_COLOR
from typing import Tuple

pygame.init()


class NameBox:
    def __init__(self, win, x, y, w, h, color, font):
        """
        Initializes the name box.
        The dimensions (x, y, w, h) are given when calling the init function.
        The default color is given when calling the init function.
        The default text is "Enter name"
        The name box is not active by default, you have to click on it to activate it.
        :param win: The screen defined in 'main'
        """
        self.win = win
        self.left, self.top, self.width, self.height = x, y, w, h
        self.font = font

        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        self.color = color
        self.text = "Enter name"
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.active = False

    def draw(self, win, color: Tuple):
        """
        Draws the rectangle and writes the name accordingly to what was typed and which color is selected
        :param color: the color that is selected in the color box
        :param win: The screen that was defined in 'main'
        """
        pygame.draw.rect(win, color, self.rect, 2)
        self.txt_surface = self.font.render(self.text, True, color)
        win.blit(
            self.txt_surface,
            (
                self.rect.x + self.rect.width // 20,
                self.rect.y + self.rect.height // 3.5,
            ),
        )

    def handle_event(self, event):
        """
        Selects the rectangle when clicked on and deletes the previous value.
        Allows the player to type its name in the rectangle as long as its active.
        The rectangle is unactivated when clicking somewhere else or pressing "Enter".
        :param event: has to be a player typing or clicking
        :return: The name that was typed by the player (or by default "Enter name" if not changed)
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.text = ""
                self.active = not self.active
            else:
                self.active = False
        self.color = WRITING_COLOR if self.active else self.color
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        self.txt_surface = self.font.render(self.text, True, self.color)
        return self.text
