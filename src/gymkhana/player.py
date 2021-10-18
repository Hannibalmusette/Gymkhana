from .constants import COLORS, FONT
import random


class Player:
    def __init__(self, win, num):
        """
        Initializes a player and gives them a random color.
        Defines a 'self.player' variable -according to the player's number-
        that will be displayed in the input box.
        :param win: The screen defined in 'main'
        :param num: 1 or 2
        """
        self.win = win
        self.num = num
        self.color = COLORS[random.randint(0, len(COLORS) - 1)]
        self.name = None
        self.player = "Player " + str(self.num) + " : "
        self.bot = False
