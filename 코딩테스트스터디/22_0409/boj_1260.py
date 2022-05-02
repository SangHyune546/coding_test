import sys
from collections import deque

input = sys.stdin.readline

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited_dfs = [False for _ in range(n+1)]
visited_bfs = [False for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in graph:
    i.sort()

def dfs(start_v):

    visited_dfs[start_v] = True
    print(start_v, end=' ')

    for i in graph[start_v]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(start_v):

    q = deque()
    q.append((start_v))
    visited_bfs[start_v] = True

    while q:

        bfs_v = q.popleft()
        print(bfs_v,end=' ')

        for i in graph[bfs_v]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True


dfs(v)
print()
bfs(v)