N, M = list(map(int, input().split()))
A = []

for n in range(N):
    s = input()
    A.append(s)

# 番号ごとに座標を分類s=0,g=10
group = []
for n in range(11):
    group.append([])
for i in range(N):
    for j in range(M):
        if A[i][j] == "S":
            n = 0
        elif A[i][j] == "G":
            n = 10
        else:
            n = int(A[i][j])
        group[n].append([i, j])

# cost[i][j]:数字を正しく通ってマス(i,j)につく最小の移動回数
cost = []
INF = 10 ** 100
for i in range(N):
    cost.append([INF] * M)

si, sj = group[0][0]
for n in range(0, 11):
    for i, j in group[n]:
        for i2, j2 in group[n - 1]:
            cost[i][j] = min(cost[i, j], cost[i2][j2] +
                             abs(i - i2) + abs(j - j2))

gi, gj = group[10][0]

ans = cost[gi][gj]
if ans == INF:
    ans = -1

print(ans)
