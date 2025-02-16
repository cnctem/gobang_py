from .player import NonePlayer


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[NonePlayer() for _ in range(size)] for _ in range(size)]

    def is_valid(self, loc):
        return 0 <= loc < self.size

    def check_win(self, x, y):
        tar = self[x, y]
        if isinstance(tar, NonePlayer): raise ValueError("Err: check NonePlayer is win?")

        for dx, dy in ((1, 0), (0, 1), (1, 1), (1, -1)):
            cnt = 1
            for i in range(1, 5):
                if (x + dx * i, y + dy * i) in self and self[x + dx * i, y + dy * i] == tar:
                    cnt += 1
                else:
                    break
            for i in range(1, 5):
                if (x - dx * i, y - dy * i) in self and self[x - dx * i, y - dy * i] == tar:
                    cnt += 1
                else:
                    break
            if cnt >= 5: return True
        return False

    def __contains__(self, loc):
        if not isinstance(loc, tuple) or len(loc) != 2 or any(map(lambda v: not isinstance(v, int), loc)): return False
        return all(map(self.is_valid, loc))

    def __getitem__(self, loc):
        # if isinstance(loc, int): return self.board[loc]
        x, y = loc
        if not all(map(self.is_valid, (x, y))): raise ValueError("out of board size")

        return self.board[x][y]

    def __setitem__(self, key, value):
        x, y = key
        self.board[x][y] = value

    def __str__(self):
        string = '  ' + ' '.join(str(chr(i % 10 + ord("0"))) for i in range(self.size)) + '\n'
        for i in range(self.size):
            string += f'{i % 10} ' + ' '.join(map(str, self.board[i])) + '\n'
        return string[:-1]
