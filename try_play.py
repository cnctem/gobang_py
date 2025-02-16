from gobang import *
from find_place import return_place
from time import sleep

def main():
    n=0
    bord_size = 16
    board = Board(bord_size)
    p1 = Player('ai', 'X', board=board)
    p2 = Player('类人', 'O', board=board)
    while True:
        n+=1
        print('===============',n,'===============')
        x,y=return_place(board,p1)
        # x,y=map(int,input('输入坐标: ').split())
        p1.put(x,y)
        print('ai 下了',(x,y),'点')
        # print(board)
        if board.check_win(x,y):
            print(p1.name,'赢了')
            break
        # inp=input()
        x,y=return_place(board,p2)
        # x,y=map(int,input('输入坐标: ').split())
        p2.put(x,y)
        print('类人 下了',(x,y),'点')
        print(board)
        if board.check_win(x,y):
            print(p2.name,'赢了')
            break
        # inp=input()
        # sleep(1)
    print(board)

if __name__ == '__main__':
    main()