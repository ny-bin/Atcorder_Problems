from collections import deque
N, M = list(map(int, input().split()))

# 辺の隣接リスト
edges = []
for i in range(N):
    edges.append([])

for i in range(M):
    u, v = list(map(int, input().split()))
    edges[u - 1].append(v - 1)
    edges[v - 1].append(u - 1)

S = int(input())
S -= 1
K = int(input())
T = list(map(int, input().split()))
for i in range(K):
    T[i] -= 1

T.append(S)
Dist = []
for t1 in T:
    INF = 10 ** 100
    dist = [INF] * N
    que = deque()
    que.append(t1)
    dist[t1] = 0
    while len(que) > 0:
        i = que.popleft()
        for j in edges[i]:
            if dist[j] == INF:
                dist[j] = dist[i] + 1
                que.append(j)
    res = []
    for t2 in T:
        res.append(dist[t2])
    Dist.append(res)

# 巡回セールスマン問題
ALL = 1 << K
cost = []
for n in range(ALL):
    cost.append([INF] * K)

for s in range(K):
    cost[1 << i][i] = Dist[K][i]


def has_bit(n, i):
    return (n & (i << i) > 0)


for n in range(ALL):
    for i in range(K):
        for j in range(K):
            if has_bit(n, j) or i == j:
                continue

            cost[n | (1 << j)][j] = min(
                cost[n | (1 << j)][j], cost[n][i] + Dist[i][j])

print(min(cost[ALL - 1]))
