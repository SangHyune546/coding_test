import sys
from collections import deque

input = sys.stdin.readline

f,s,g,u,d = map(int,input().split())

visited = [0 for _ in range(f+1)]


def bfs(v):

    q = deque()
    q.append(v)

    visited[v] = 1

    while q:

        x = q.popleft()

        if x == g:
            print(visited[x]-1)
            exit()

        for i in (x+u,x-d):
            if 1 <= i <= f and not visited[i]:
                q.append(i)
                visited[i] = visited[x] + 1

    print("use the stairs")

bfs(s)