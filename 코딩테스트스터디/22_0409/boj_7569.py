import sys
from collections import deque

input = sys.stdin.readline


m,n,h = map(int,input().split())

graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

tq = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                tq.append([i, j, k])

dx=[1,0,-1,0,0,0]
dy=[0,1,0,-1,0,0]
dz=[0,0,0,0,1,-1]

while tq:

    z,x,y = tq.popleft()

    for i in range(len(dx)):

        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0<=nz<h and 0<=nx<n and 0<=ny<m and graph[nz][nx][ny] == 0:
            tq.append((nz,nx,ny))
            graph[nz][nx][ny] = graph[z][x][y] +1
            
answer = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit()
            answer = max(answer,graph[i][j][k])

print(answer-1)
        
