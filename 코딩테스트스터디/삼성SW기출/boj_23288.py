import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

dice = {'up':2,'top':1,'left':4,'right':3,'down':5,'bottom':6}

dx = [-1,0,1,0]
dy = [0,1,0,-1]

answer = 0

def dice_rotate(d):
    if d == 0:

    elif d == 1:

    elif d == 2:
    
    else:
        

