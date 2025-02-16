from typing import List, Optional, Tuple

from gobang.player import Player

BoardItem = Optional[Player]


class Board:
    size: int
    board: List[List[BoardItem]]

    def __init__(self, size: int) -> None: ...

    def is_valid(self, loc: int) -> bool: ...

    def check_win(self, x: int, y: int) -> bool: ...

    def __contains__(self, loc: Tuple[int, int]) -> bool: ...

    def __getitem__(self, loc: Tuple[int, int]) -> BoardItem: ...

    def __setitem__(self, key: Tuple[int, int], value: BoardItem) -> None: ...

    def __str__(self) -> str: ...
