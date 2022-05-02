import sys
from collections import deque

n,m = map(int,input().split())

graph = [list(map(int,input().rstrip())) for _ in range(n)]
visited = [[0] * (m) for _ in range(n)]

visited[0][0] = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):

    q = deque()
    q.append((x,y))

    while q:

        x,y = q.popleft()

        for i in range(len(dx)):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[-1][-1]


def v_bfs(x,y):


    q = deque()
    q.append((x,y))

    while q:

        x,y = q.popleft()

        if x == n-1 and y == m-1:
            print(visited[x][y])
            break

        for i in range(len(dx)):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1



#print(bfs(0,0))
v_bfs(0,0)



