import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [list(map(int,input().rstrip())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y,graph):

    q = deque()
    q.append((x,y))

    graph[x][y] = 0

    count = 1

    while q:

        x,y = q.popleft()

        for i in range(len(dx)):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] =0
                count +=1

    return count


def dfs(x,y,graph):

    global count

    graph[x][y] = 0 
    count +=1

    for i in range(len(dx)):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(nx,ny,graph)
            

ans_list = list()

'''
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            ans_list.append(bfs(i,j,graph))'''


count = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            dfs(i,j,graph)
            ans_list.append(count)
            count = 0


ans_list.sort()

print(len(ans_list))

for i in ans_list:
    print(i)
