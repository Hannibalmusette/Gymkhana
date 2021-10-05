from .constants import COLORS
import random

class Player:
    def __init__(self, num):
        self.num = num
        self.name = input("Enter player_" + str(self.num) + "'s name : ")
        self.color = COLORS.pop(random.randint(0, len(COLORS)-1))