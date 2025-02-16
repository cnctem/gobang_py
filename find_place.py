from gobang import *
import random
from copy import deepcopy

def my_max(arrarr):
    max_num = max(arrarr[0])
    for arr in arrarr:
        if max(arr) > max_num:
            max_num = max(arr)
    return max_num

def point_score(self, x, y, tar): # tar 是被判定棋子的类型
        quan = 0.25
        score = 0
        for dx, dy in ((1, 0), (0, 1), (1, 1), (1, -1)):
            cnt = 1
            head=tail=True
            for i in range(1, 6):
                if (x + dx * i, y + dy * i) in self and self[x + dx * i, y + dy * i] == tar:
                    cnt += 1
                elif (x + dx * i, y + dy * i) in self and bool(self[x,y])==False:
                    break
                else:
                    cnt -= quan
                    head=False
                    break
            for i in range(1, 6):
                if (x - dx * i, y - dy * i) in self and self[x - dx * i, y - dy * i] == tar:
                    cnt += 1
                elif (x - dx * i, y - dy * i) in self and bool(self[x,y])==False:
                    break
                else:
                    cnt -= quan
                    tail=False
                    break
            if cnt+quan*2>=5:
                score += 100**(cnt+quan*2)
            elif head or tail:
                score += 100**cnt
        return score

def random_pick(self,choice_list):
    if len(choice_list)==0 or len(choice_list)>=self.size**2//2:
        while True:
            x=random.randint(self.size//4,3*self.size//4-1)
            y=random.randint(self.size//4,3*self.size//4-1)
            if bool(self[x,y])==False:
                return x,y
    else:
        x,y=random.choice(choice_list)
        return x,y

def mind_pick(self,choice_list,tar):
    if len(choice_list)==0 or len(choice_list)>=self.size**2//2:
        while True:
            x=random.randint(self.size//4,3*self.size//4-1)
            y=random.randint(self.size//4,3*self.size//4-1)
            if bool(self[x,y])==False:
                return x,y
    elif len(choice_list)==1:
        return choice_list[0]
    else:
        flag=True
        for x,y in choice_list:
            try_board=deepcopy(self)
            try_board[x,y]=tar
            try_score=return_score(try_board,tar)
            if flag:
                max_score=try_score
                max_x,max_y=x,y
                flag=False
            elif try_score>max_score:
                max_score=try_score
                max_x,max_y=x,y
        return max_x,max_y

def max_score_list(score_board):
    quan=0.6
    max_score=my_max(score_board)
    choice_list=[]
    for i in range(len(score_board)):
        for j in range(len(score_board)):
            if score_board[i][j]//(max_score**quan)==max_score//(max_score**quan):
                choice_list.append((i,j))
    return choice_list

def find_other(self,tar):
    for i in range(self.size):
        for j in range(self.size):
            if bool(self[i,j]) and self[i,j]!=tar:
                return self[i,j]
    return None


def return_score(self,tar):
    other_player=find_other(self,tar)
    score_board = [[0 for i in range(self.size)] for j in range(self.size)]
    for i in range(self.size):
        for j in range(self.size):
            if bool(self[i,j])==False:
                score_board[i][j] = point_score(self, i, j, tar)*2
                if other_player:
                    score_board[i][j] -= point_score(self, i, j, other_player)
    return my_max(score_board)

def return_place(self,tar):
    other_player=find_other(self,tar)
    score_board = [[0 for i in range(self.size)] for j in range(self.size)]
    for i in range(self.size):
        for j in range(self.size):
            if bool(self[i,j])==False:
                score_board[i][j] = point_score(self, i, j, tar)*10
                if other_player:
                    score_board[i][j] += point_score(self, i, j, other_player)
    max_list=max_score_list(score_board)
    # if len(max_list)<=19:
    #     print(max_list)
    return random_pick(self,max_list)
    # return mind_pick(self,max_list,tar)