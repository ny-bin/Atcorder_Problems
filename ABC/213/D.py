import sys
import heapq
from collections import deque
sys.setrecursionlimit(1000000)

N = int(input())
visited = [False] * (N + 1)


# 各都市から出ている都市
all_city_list: list = []
for n in range(N + 1):
    all_city_list.append([])


# 今の都市
now_city = 1
before_city = 0
ans = []


def dfs(i, x):
    visited[i] = True
    print(i, end=' ')

    city_list = all_city_list[i]
    if len(city_list) == 0:
        return

    while len(city_list) > 0:
        city = heapq.heappop(city_list)
        if not visited[city]:
            dfs(city, i)

    if x != 0:
        print(x, end=' ')


for n in range(N - 1):
    A, B = map(int, input().split())
    heapq.heappush(all_city_list[A], B)
    heapq.heappush(all_city_list[B], A)

dfs(1, 0)
