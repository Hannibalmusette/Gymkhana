import pygame

from .write_text import write_text

pygame.init()


class NameBox:
    def __init__(self, x, y, w, h):
        self.active = False
        self.text = "Enter name"
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, win, color):
        pygame.draw.rect(win, color, self.rect, 2)
        write_text(
            self.text, self.rect.x, self.rect.y, self.rect.w, self.rect.h, color=color
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.text = ""
            self.active = True
        elif event.type == pygame.MOUSEBUTTONDOWN and not self.rect.collidepoint(
            event.pos
        ):
            self.active = False

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
