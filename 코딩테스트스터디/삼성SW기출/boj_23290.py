import sys
from collections import deque,defaultdict
from copy import deepcopy


input = sys.stdin.readline


m,s = map(int,input().split()) # 물고기 마릿수 - m , 상어가 마법을 연습한 횟수 S

n = 4 #4x4 크기의 격자에서 진행할것

shark = -1
smell = -2

board = [[0] * n for _ in range(n)]

fish_info = list()


'''
1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
1: ←
2: ↖
3:  ↑
4: ↗
5: →
6: ↘
7: ↓
8: ↙
'''
fish_dx = [0,-1,-1,-1,0,1,1,1]
fish_dy = [-1,-1,0,1,1,1,0,-1]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

dir_dict = defaultdict(list)

for i in range(1,9):
    dir_dict[i] = [fish_dx[i-1],fish_dy[i-1]]

for _ in range(m):

    fx,fy,d = map(int,input().split())
    board[fx-1][fy-1] = d

sx,sy = map(int,input().split())
sx -= 1
sy -= 1

board[sx][sy] = shark

def copy_magic():

    new_board = deepcopy(board)

def move_fish():

    rboard = [[0]*n for _ in range(n)]

    temp_info = deepcopy(fish_info)

    for i in range(n):
        for j in range(n):
            while board[i][j]:
                fish_dir = temp_info[i][j].pop()
                print(fish_dir)



    return rboard

rboard = move_fish()







