import pygame

from gymkhana.choices import write_text
from gymkhana.constants.constants import MARGIN, WHITE, WIN


def player_and_triangle(player_1, player_2, win=WIN, margin=MARGIN):
    som_i = margin * 3
    som_j = margin * 2.5
    bas_i_1 = margin * 2.5
    bas_i_2 = margin * 3.5
    bas_j = margin

    pygame.draw.polygon(
        win,
        player_1.color,
        ((bas_i_1, bas_j), (bas_i_2, bas_j), (som_i, som_j)),
    )
    pygame.draw.polygon(
        win,
        player_2.color,
        ((bas_j, bas_i_1), (bas_j, bas_i_2), (som_j, som_i)),
    )
    write_text(
        "1", margin * 2.8, margin * 1.5, margin // 2.5, margin // 2.5, color=WHITE
    )
    write_text(
        "2",
        margin * 1.5,
        margin * 2.8,
        margin // 2.5,
        margin // 2.5,
        color=WHITE,
        rotate=True,
    )
    write_text(
        player_1.name,
        bas_i_2,
        margin // 3,
        margin // 1.5,
        margin // 1.5,
        color=player_1.color,
    )
    write_text(
        player_2.name,
        margin // 3,
        bas_i_2,
        margin // 1.5,
        margin // 1.5,
        color=player_2.color,
        rotate=True,
    )
