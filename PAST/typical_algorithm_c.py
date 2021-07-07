N = int(input())
A = []
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

ALL = 1 << N

# cost[n][i]:訪れた都市の集合nと最後の都市がiであるときのコストの最小値
cost = []
for n in range(ALL):
    cost.append([10**100] * N)

# 初期条件
cost[0][0] = 0


def has_bit(n, i):
    return (n & (1 << i) > 0)


for n in range(ALL):
    for i in range(N):
        # iからjに移動する遷移を試す
        for j in range(N):
            if has_bit(n, j) or i == j:
                continue
            cost[n | (1 << j)][j] = min(
                cost[n | (i << j)][j], cost[n][i] + A[i][j])

print(cost[ALL - 1][0])
