from typing import Tuple

GREY = (70, 75, 80)
GREEN = (40, 65, 35)
BLUE = (40, 65, 80)
INDIGO = (55, 55, 85)
VIOLET = (70, 35, 60)
ORANGE = (85, 50, 25)

COLORS = [GREY, GREEN, BLUE, INDIGO, VIOLET, ORANGE]
COLORS_DICT = {v: k for k, v in locals().items() if isinstance(v, Tuple)}
