import sys
from collections import deque

n,k = map(int,input().split())

visited = [0 for _ in range(100001)]


def bfs(v):

    q = deque()
    q.append((v))
    visited[v] = 1

    while q:

        x = q.popleft()

        if x == k:
            print(visited[x]-1)
            exit()

        for i in (x-1,x+1,x*2):
            if 0 <= i <= 100000 and visited[i] == 0:
                q.append((i))
                visited[i] = visited[x] + 1

bfs(n)