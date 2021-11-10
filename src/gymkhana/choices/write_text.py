import pygame
from gymkhana.constants import WIN, FONT, WRITING_COLOR

def write_text(txt: str, x, y, w, h, rend=True, font=FONT, color=WRITING_COLOR, thick=2, win=WIN):
    text = font.render(txt, rend, color)
    rect = text.get_rect()
    rect.center = (x + w // 2, y + h // 2)
    win.blit(text, rect)