N, W = list(map(int, input().split()))

# 1始まりにする
ws = [0]
vs = [0]

for i in range(N):
    w, v = list(map(int, input().split()))
    ws.append(w)
    vs.append(v)

# value[i][w]:品物iまで見て重さ合計wであるときの価値の総和の最大値

value = []
for i in range(N + 1):
    value.append([-10 * 18] * (W + 1))

# 初期条件
value[0][0] = 0

# iが小さい順に求めていく
for i in range(1, N + 1):
    for w in range(W + 1):
        # 品物iを使わない
        value[i][w] = max(value[i][w], value[i - 1][w])
        # 品物iを使う
        if w - ws[i] >= 0:
            value[i][w] = max(value[i][w], value[i - 1][w - ws[i]] + vs[i])

ans = max(value[N])
print(ans)
