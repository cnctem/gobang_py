from gobang import *
from find_place import point_score
from copy import deepcopy
bord_size = 16
board = Board(bord_size)
new_board = deepcopy(board)
score_board = [[0 for i in range(bord_size)] for j in range(bord_size)]
#print(score_board)

def main():
    board = Board(bord_size)
    p = Player('戴波爷', 'X', board=board)
    p2 = Player('戴波爷2', 'O', board=board)
    # print((6, 15) in board)
    # p.put(0, 0)
    # print(p == board[0, 0])
    print(board[1, 1])
    print(bool(board[1, 1]))
    p.put(1, 1)
    print(board[1, 1].name)
    print(type(board[1, 1]))
    print(bool(board[1, 1]))
    print(p==board[1, 1])
    
    

    print(point_score(board, 1, 1, p))


   

    for i in range(bord_size):
        for j in range(bord_size):
            #print(point_score(board, 1, 1, p))
            if not board[i, j]: p.put(i, j)
    a=board.check_win(1,1)
    print(point_score(board, 1, 1, p))
    print(666,a)
    print(board)
if __name__ == '__main__':
    main()