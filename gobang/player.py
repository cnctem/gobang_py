class Player:
    def __init__(self, name, style, board):
        super().__init__()
        self.name = name
        self.style = style
        self.board = board

    def __bool__(self):
        return True

    def __repr__(self):
        return self.style

    def __str__(self):
        return self.__repr__()

    def put(self, x, y):
        self.board[x, y] = self


class NonePlayer(Player):
    def __init__(self):
        super().__init__("?", "·", board=None)

    def __bool__(self):
        return False
