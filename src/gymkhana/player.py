from typing import Tuple
from dataclasses import dataclass

@dataclass
class Player:
    num: int
    color: Tuple
    name: str
    bot: bool