from .constants import COLORS, FONT
import random


class Player:
    def __init__(self, win, num):
        self.win = win
        self.num = num
        self.font = FONT
        self.color = COLORS[random.randint(0, len(COLORS) - 1)]
        self.name = None
        self.player = "Player " + str(self.num) + " : "
