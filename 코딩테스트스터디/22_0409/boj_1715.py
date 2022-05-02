import sys
import heapq

input = sys.stdin.readline

n = int(input())

deck = list()

for _ in range(n):
    heapq.heappush(deck,int(input()))

if len(deck) == 1:
    print(0)

else:
    answer = 0

    while len(deck) > 1:

        tmp1 = heapq.heappop(deck)
        tmp2 = heapq.heappop(deck)

        answer += tmp1 + tmp2
        heapq.heappush(deck,answer)

    print(answer)

