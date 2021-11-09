from gymkhana.constants import COLORS, FONT
import random


class Player:
    def __init__(self, num):
        self.num = num
        self.color = COLORS[random.randint(0, len(COLORS) - 1)]
        self.name = None
        self.bot = False
