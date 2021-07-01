# N = int(input())
# num = list(map, input().split())

# cost = [0] * N

# # 初期条件
# cost[0] = 0

# # 2番目も最初にわかる
# cost[1] = cost[0] + abs(num[0] - num[1])

# for i in range(2, N):
#     cost[i] = min(cost[i - 1] + abs(num[i - 1] - num[i]),
#                   cost[i - 2] + abs(num[i - 2] - num[i]))

# print(cost[N - 1])

import sys
sys.setrecursionlimit(1000000)
N = int(input())
h = list(map(int, input().split()))
cost = [0] * N
done = [False] * N


def rec(i):
    if done[i]:
        return cost[i]

    if i == 0:
        cost[i] = 0
    elif i == 1:
        cost[i] = rec(0) + abs(h[0] - h[1])
    else:
        cost[i] = min(rec(i - 1) + abs(h[i - 1] - h[i]),
                      rec(i - 2) + abs(h[i - 2] - h[i]))
    done[i] = True
    return cost[i]


print(rec(N - 1))
