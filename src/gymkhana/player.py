from .constants import COLORS, BG_COLOR, WIDTH, HEIGHT
import random
import pygame
from gymkhana.inputbox import InputBox


class Player:
    def __init__(self, win, num):
        self.win = win
        self.num = num
        self.color = COLORS[random.randint(0, len(COLORS) - 1)]
        self.name = None
        self.player = "Player " + str(self.num) + " : "
        self.color, self.name = self.choice(win, self.player)

    def choice(self, win, player):
        input_box = InputBox(
            self.win, WIDTH // 18, HEIGHT // 8, WIDTH * 9 // 10, HEIGHT // 2, player
        )

        done = None

        color, name = self.color, self.name

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and input_box.is_ready(event):
                    done = True
                else:
                    color, name = input_box.handle_event(event)

            win.fill(BG_COLOR)

            input_box.draw(win)

            pygame.display.flip()

        return color, name
