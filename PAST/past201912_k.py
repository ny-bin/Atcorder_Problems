import sys
sys.setrecursionlimit(100000)

N = int(input())
R = -1
#edges[i] : 頂点iの部下の頂点番号
edges = []
for i in range(N):
    edges.append([])

for i in range(N):
    p = int(input())
    if p == -1:
        R = i
    else:
        edges[p - 1].append(i)


queries = []
for i in range(N):
    queries.append([])

Q = int(input())
for q in range(Q):
    a, b = list(map(int, input().split()))
    queries[a - 1].append([q, b - 1])

ans = [False] * Q
boss = [False] * N


def dfs(i):
    for q, b in queries[i]:
        ans[q] = boss[b]

    # 自身を上司に設定
    boss[i] = True
    # 再帰的に子を見ていく
    for j in edges[i]:
        dfs(j)
    # 抜ける時に自信を上司から外す
    boss[i] = False


dfs(R)

for q in range(Q):
    if ans[q]:
        print('Yes')
    else:
        print("No")
