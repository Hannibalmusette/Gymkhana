import pygame
from .write_text import write_text

pygame.init()


class TickBot:
    def __init__(self, x: int, y: int, w: int, h: int):
        self.left, self.top, self.width, self.height = x, y, w, h
        self.rect = pygame.Rect(self.left, self.top, self.height, self.height)
        self.radius = self.height // 2
        self.bot = False

    def draw(self, win, color):
        pygame.draw.rect(win, color, self.rect, 2)
        write_text("Bot", self.left, self.top, self.width, self.height, color=color)
        if self.bot:
            pygame.draw.circle(
                win,
                color,
                (self.left + self.radius, self.top + self.radius),
                self.radius,
            )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.bot = True if not self.bot else False
