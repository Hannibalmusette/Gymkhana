import pygame
import random
from .write_text import write_text
from .inputbox import InputBox
from gymkhana.constants import WIDTH, HEIGHT, WIN, WRITING_COLOR, BG_COLOR, COLORS

pygame.init()

def random_colors(colors=COLORS):
    color_1 = random.choice(colors)
    color_2 = random.choice(colors)
    while color_1 == color_2:
        color_2 = random.choice(colors)
    return color_1, color_2

def make_rect(x, y, w, h):
    return pygame.Rect(x, y, w, h)

def draw_rect(rect, color=WRITING_COLOR, win=WIN):
    pygame.draw.rect(win, color, rect, 2)

def button_clicked(event, button) -> bool:
    return event.type == pygame.MOUSEBUTTONDOWN and button.collidepoint(
        event.pos
    )

def choices(win=WIN, bgcolor=BG_COLOR, width=WIDTH, height=HEIGHT):
    color_1, color_2 = random_colors()
    input_box_1 = InputBox(1, color_1)
    input_box_2 = InputBox(2, color_2)

    x = width//3
    y = height//1.5
    w = width//3
    h = height//10
    ready_button = make_rect(x, y, w, h)

    done = False

    while not done:
        win.fill(bgcolor)
        input_box_1.draw()
        input_box_2.draw()

        draw_rect(ready_button)
        write_text("READY", x, y, w, h)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif button_clicked(event, ready_button) and color_1 != color_2:
                done = True
            else:
                choices_1 = input_box_1.handle_event(event)
                choices_2 = input_box_2.handle_event(event)

    return choices_1, choices_2