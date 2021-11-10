from gymkhana.constants import COLORS, FONT
import random


class Player:
    def __init__(self, num):
        self.num = num
        self.color = random.choice(COLORS)
        self.name = None
        self.bot = False
