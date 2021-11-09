import pygame

pygame.init()


class TickBot:
    def __init__(self, win, x: int, y: int, w: int, h: int, color, font):
        self.win = win
        self.font = font
        self.color = color
        self.left, self.top, self.width, self.height = x, y, w, h
        self.bot = False

        self.txt = self.font.render("Bot", True, self.color)
        self.rect = self.txt.get_rect()
        self.rect.center = (self.left + 2 * self.width // 3, self.top)

        self.tick_square = pygame.Rect(
            self.left, self.top - self.height // 2, self.height, self.height
        )
        self.tick_radius = self.height // 2

    def draw(self, win, color):
        self.color = color
        self.txt = self.font.render("Bot", True, self.color)
        win.blit(self.txt, self.rect)
        pygame.draw.rect(self.win, self.color, self.tick_square, 1)
        if self.bot:
            pygame.draw.circle(
                self.win,
                color,
                (self.left + self.tick_radius, self.top),
                self.tick_radius,
            )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.tick_square.collidepoint(
            event.pos
        ):
            self.bot = True if not self.bot else False

        return self.bot
