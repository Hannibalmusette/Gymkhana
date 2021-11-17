import pygame

from gymkhana.constants import FONT, WIN, WRITING_COLOR


def write_text(
    txt: str,
    x: int,
    y: int,
    w: int,
    h: int,
    rotate=False,
    rend=True,
    font=FONT,
    color=WRITING_COLOR,
    win=WIN,
):
    text = font.render(txt, rend, color)
    if rotate:
        text = pygame.transform.rotate(text, 90)
    rect = text.get_rect()
    rect.center = (x + w // 2, y + h // 2)
    win.blit(text, rect)
