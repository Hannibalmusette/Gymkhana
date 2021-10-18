import pygame
import random
from gymkhana.constants import COLORS, WHITE
from typing import Tuple

pygame.init()


class ColorBox:
    def __init__(self, win, x: int, y: int, w: int, h: int):
        """
        Initializes the colorbox.
        The dimensions (x, y, w, h) are given when calling the init function.
        The colors are defined in the 'constants'.
        The radius is calculated according to the number of colors.
        One of the colors is selected by default
        'self.circles' is a list that will be updated when the color circles are drawn.
        :param win: The screen defined in 'main'
        """
        self.win = win
        self.left, self.top, self.width, self.height = x, y, w, h

        self.colors = COLORS
        self.radius = self.width // len(self.colors) // 2.3
        self.select = self.colors[random.randint(0, len(COLORS) - 1)]
        self.circles = []

    def draw_circle(self, color: Tuple, n: int, select=None):
        """
        This function is called each time we want to draw a colored circle.
        :param color: The color of the circle
        :param n: The number in the list of colors : allows to calculate the circle's position.
        :param select: If the circle is selected, another wider circle will be first drawn behind him.
        :return: The circle's position (x, y) and its color.
        """
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
        """
        Calls the draw function to draw a circle for each color in the list.
        Uses a parameter 'n' that is the position of the color in the list
        to help determines each circle's position.
        If the color is selected, calls the function twice to draw a wider, white circle first.
        Updates the list of circles that contains the position and color of each of them.
        """
        n = 0
        for color in self.colors:
            n += 1
            if color == self.select:
                self.draw_circle(WHITE, n, select=True)
            circle = self.draw_circle(color, n)
            self.circles.append(circle)

    def handle_event(self, event):
        """
        When a player clicks inside of a circle, its color is selected.
        :param event: has to be a player clicking.
        :return: The selected color
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            for circle in self.circles:
                x2, y2 = circle[0]
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 < self.radius ** 2:
                    self.select = circle[1]
        return self.select
