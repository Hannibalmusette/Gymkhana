from typing import Tuple

import pygame

from gymkhana.constants import COLORS, WHITE, WIN

pygame.init()


class ColorBox:
    def __init__(self, color, x: int, y: int, w: int, h: int, colors=COLORS):
        self.left, self.top, self.width, self.height = x, y, w, h
        self.select = color
        self.radius = int(self.width // len(colors) // 2.3)
        self.circles = {
            self.circle_coord(n + 1): color for n, color in enumerate(colors)
        }

    def circle_coord(self, n: int) -> Tuple[int]:
        x = self.radius * n * 2.3
        y = self.top + self.height // 2
        return int(x), int(y)

    def draw_circle(self, color: Tuple, coord, select=False, win=WIN):
        radius = self.radius + 2 if select else self.radius
        pygame.draw.circle(win, color, coord, radius)

    def draw_circles(self, highlight_color=WHITE):
        for circle in self.circles:
            if self.circles[circle] == self.select:
                self.draw_circle(highlight_color, circle, select=True)
            self.draw_circle(self.circles[circle], circle)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            for circle in self.circles:
                x, y = circle
                if (x1 - x) ** 2 + (y1 - y) ** 2 < self.radius ** 2:
                    self.select = self.circles[circle]
                    break
