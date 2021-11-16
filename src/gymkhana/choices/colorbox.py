import pygame
import random
from gymkhana.constants import COLORS, WHITE, WIN
from typing import Tuple

pygame.init()


class ColorBox:
    def __init__(self, color, x: int, y: int, w: int, h: int, colors=COLORS):
        self.left, self.top, self.width, self.height = x, y, w, h
        self.select = color
        self.radius = self.width // len(colors) // 2.3
        self.circles = []
        self.colors = colors

    def draw_circle(self, color: Tuple, n: int, select=None, win=WIN):
        radius = self.radius
        x = radius * n * 2.3
        y = self.top + self.height // 2
        if select:
            radius += 2
        pygame.draw.circle(
            win,
            color,
            (x, y),
            radius,
        )
        return (x, y), color

    def update_list(self, circle):
        self.circles.append(circle)

    def draw_circles(self, highlight_color=WHITE):
        n = 0
        for color in self.colors:
            n += 1
            if color == self.select:
                self.draw_circle(highlight_color, n, select=True)
            circle = self.draw_circle(color, n)
            self.update_list(circle)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            for circle in self.circles:
                x2, y2 = circle[0]
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 < self.radius ** 2:
                    self.select = circle[1]
