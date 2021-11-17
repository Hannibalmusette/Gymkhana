import random
from typing import List, Tuple

import pygame

from gymkhana.constants import (BG_COLOR, COLORS, HEIGHT, WIDTH, WIN,
                                WRITING_COLOR)

from .inputbox import InputBox
from .write_text import write_text

pygame.init()


def random_colors(colors: List = COLORS) -> Tuple[Tuple]:
    color_1 = random.choice(colors)
    color_2 = random.choice(colors)
    while color_1 == color_2:
        color_2 = random.choice(colors)
    return color_1, color_2


def make_rect(x: int, y: int, w: int, h: int) -> pygame.Rect:
    return pygame.Rect(x, y, w, h)


def draw_rect(rect: pygame.Rect, color=WRITING_COLOR, win=WIN):
    pygame.draw.rect(win, color, rect, 2)


def button_clicked(event, button: pygame.Rect) -> bool:
    return event.type == pygame.MOUSEBUTTONDOWN and button.collidepoint(event.pos)


def draw(input_box_1, input_box_2, button: pygame.Rect, txt, win=WIN, bgcolor=BG_COLOR):
    win.fill(bgcolor)
    input_box_1.draw()
    input_box_2.draw()
    draw_rect(button)
    write_text(*txt)
    pygame.display.flip()


def choices(width: int = WIDTH, height: int = HEIGHT) -> Tuple:
    color_1, color_2 = random_colors()
    input_box_1 = InputBox(1, color_1)
    input_box_2 = InputBox(2, color_2)

    x = width // 3
    y = height // 1.5
    w = width // 3
    h = height // 10
    ready_button = make_rect(x, y, w, h)
    ready_txt = ("Ready", x, y, w, h)

    done = False

    while not done:
        draw(input_box_1, input_box_2, ready_button, ready_txt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif button_clicked(event, ready_button) and color_1 != color_2:
                done = True
            else:
                choices_1 = input_box_1.handle_event(event)
                choices_2 = input_box_2.handle_event(event)

    return choices_1, choices_2
