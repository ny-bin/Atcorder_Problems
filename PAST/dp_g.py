import sys
sys.setrecursionlimit(1000000)

N, M = list(map(int, input().split()))

#edges[i]: 頂点iから伸びている頂点たち
edges = []
for i in range(N):
    edges.append([])

# 入字数。始点の判定に使う
indeg = [0] * N

# 辺の入力を受け取り、隣接リストを作成
for i in range(M):
    x, y = list(map(int, input().split()))

    edges[x - 1].append(y - 1)
    indeg[y - 1] += 1

# 頂点iから始まるパスの最大長
length = [0] * N

done = [False] * N


def rec(i):
    if done[i]:
        return length[i]

    length[i] = 0
    for j in edges[i]:
        length[i] = max(length[i], rec(j) + 1)

    done[i] = True
    return length[i]


for i in range(N):
    if indeg[i] == 0:
        rec(i)

print(max(length))
