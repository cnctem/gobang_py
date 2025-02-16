from typing import Optional

from .board import Board


class Player:
    name: str
    style: str
    board: Optional[Board]

    def __init__(self, name: str, style: str, board: Optional[Board]):
        super().__init__()

    def __bool__(self) -> True: ...

    def __repr__(self) -> str: ...

    def __str__(self) -> str: ...

    def put(self, x: int, y: int) -> bool: ...


class NonePlayer(Player):
    def __init__(self):
        super().__init__("?", "·", board=None)

    def __bool__(self) -> False: ...
