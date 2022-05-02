import sys
from collections import deque

input = sys.stdin.readline


m,n = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

tq = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            tq.append([i, j])

dx=[1,0,-1,0]
dy=[0,1,0,-1]

while tq:

    x,y = tq.popleft()

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
            tq.append((nx,ny))
            graph[nx][ny] = graph[x][y] +1
            
answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
        answer = max(answer,graph[i][j])

print(answer-1)
        
