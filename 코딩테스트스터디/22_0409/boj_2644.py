import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

ref,target = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

m = int(input())

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):

    q = deque()
    q.append((v))

    visited[v] = 1

    while q:
        
        bfs_v = q.popleft()

        for i in graph[bfs_v]:
            if visited[i] == 0:
                q.append((i))
                visited[i] += (visited[bfs_v] + 1)

bfs(ref)

if visited[target] != 0:
    print(visited[target]-1)
else:
    print(-1)