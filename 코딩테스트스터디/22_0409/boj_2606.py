import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)


for i in graph:
    i.sort()

def dfs(v):

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):

    q = deque()
    q.append((v))

    visited[v] = True

    while q:
        
        bfs_v = q.popleft()

        for i in graph[bfs_v]:
            if not visited[i]:
                q.append((i))
                visited[i] = True


bfs(1)

print(visited.count(True)-1)