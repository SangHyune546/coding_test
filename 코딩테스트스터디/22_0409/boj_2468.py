import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

max_num = max(max(graph))

max_list = []

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def bfs(x,y,rain):

    q = deque()
    q.append((x,y))

    visited[x][y] = True

    while q:

        x,y = q.popleft()

        for i in range(len(dx)):

            nx = x + dx[i]
            ny = y + dy[i] 

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > rain and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True


for k in range(max_num):

  visited = [[False] * n for _ in range(n)]
  count = 0

  for i in range(n):
    for j in range(n):
      if graph[i][j] > k and not visited[i][j]:
          bfs(i,j,k)
          count += 1

  max_list.append(count)

print(max(max_list))
    
