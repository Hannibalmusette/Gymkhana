import pygame
from gymkhana.constants import WRITING_COLOR

pygame.init()


class NameBox:
    def __init__(self, win, x, y, w, h, color, font):
        self.win = win
        self.left, self.top, self.width, self.height = x, y, w, h
        self.font = font

        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        self.color = color
        self.text = "Enter name"
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.active = False
        self.answer = None

    def draw(self, win, color):
        # Blit the rect.
        pygame.draw.rect(win, color, self.rect, 2)

        # Blit the text inside the box.
        self.txt_surface = self.font.render(self.text, True, color)
        win.blit(
            self.txt_surface,
            (
                self.rect.x + self.rect.width // 20,
                self.rect.y + self.rect.height // 3.5,
            ),
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                self.text = ""
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
        self.color = WRITING_COLOR if self.active else self.color
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
        self.txt_surface = self.font.render(self.text, True, self.color)
        return self.text
