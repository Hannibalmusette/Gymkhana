import pygame
import random
from gymkhana.constants import COLORS, WHITE

pygame.init()


class ColorBox:
    def __init__(self, win, x, y, w, h):
        self.win = win
        self.left, self.top, self.width, self.height = x, y, w, h

        self.colors = COLORS
        self.radius = self.width // len(self.colors) // 2.3
        self.select = self.colors[random.randint(0, len(COLORS) - 1)]
        self.circles = []
        self.answer = None

    def draw_circle(self, color, n, select=None):
        radius = self.radius
        x = radius * n * 2.3
        y = self.top + self.height // 2
        if select:
            radius += 2
        pygame.draw.circle(
            self.win,
            color,
            (x, y),
            radius,
        )
        return (x, y), color

    def draw_circles(self):
        n = 0
        for color in self.colors:
            n += 1
            if color == self.select:
                self.draw_circle(WHITE, n, select=True)
            circle = self.draw_circle(color, n)
            self.circles.append(circle)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            x1, y1 = event.pos
            for circle in self.circles:
                x2, y2 = circle[0]
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 < self.radius ** 2:
                    self.select = circle[1]
        return self.select
