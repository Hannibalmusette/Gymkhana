import pygame

pygame.init()


class TickBot:
    def __init__(self, win, x: int, y: int, w: int, h: int, color, font):
        """
        Initializes a box that allows to tick whether the player should be a bot or not.
        The dimensions (x, y, w, h) are given when calling the init function.
        The player is by default not a bot.
        :param win: The screen defined in 'main'
        """
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
        """
        Selects the rectangle when clicked on and deletes the previous value.
        Allows the player to type its name in the rectangle as long as its active.
        The rectangle is unactivated when clicking somewhere else or pressing "Enter".
        :param event: has to be a player typing or clicking
        :return: The name that was typed by the player (or by default "Enter name" if not changed)
        """
        if event.type == pygame.MOUSEBUTTONDOWN and self.tick_square.collidepoint(
            event.pos
        ):
            self.bot = True if not self.bot else False

        return self.bot
