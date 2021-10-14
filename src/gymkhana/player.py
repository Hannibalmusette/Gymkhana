from .constants import COLORS, BG_COLOR, WRITING_COLOR, WIDTH, HEIGHT, FONT
import random
import pygame
from gymkhana.inputbox import InputBox


class Player:
    def __init__(self, win, num):
        self.win = win
        self.num = num
        self.font = FONT
        self.color = COLORS[random.randint(0, len(COLORS) - 1)]
        self.name = None
        self.player = "Player " + str(self.num) + " : "
