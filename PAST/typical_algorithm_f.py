import heapq

N, M = map(int, input().split())

# 隣接リストとしてグラフの情報を保持する配列
G = []
for _ in range(0, N):
    G.append([])

for _ in range(0, M):
    u, v, c = map(int, input().split())

    # 頂点uから出てvへ向かう重みcの辺を保存する
    G[u].append((v, c))
    # 無向グラフのため反対向きにも保存
    G[v].append((u, c))

# プリム法で最小全域木問題を解く
# 頂点がマークされているかを判別する配列
marked = []
for _ in range(0, N):
    marked.append(False)

# マークされている頂点の数を保持
marked_count = 0

marked[0] = True
marked_count += 1

# 次に選ぶ辺の候補を入れる

Q = []

for j, c in G[0]:
    heapq.heappuhs(Q, (c, j))

sum = 0

while marked_count < N:
    c, i = heapq.heappop(Q)

    if marked[i]:
        continue

    marked[i] = True
    marked_count += 1

    sum += c

    for (j, c) in G[i]:
        if marked[j]:
            continue

        heapq.heappop(Q, (c, j))
print(sum)
