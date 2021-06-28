from collections import deque

R, C = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))
S = []

for i in range(R):
    s = input()
    S.append(s)

# 座標をリストの形式に合わせる
sy -= 1
sx -= 1
gy -= 1
gx -= 1

# 始点から最小移動回数を管理する二次元配列
dist = []
for i in range(R):
    dist.append([-1] * C)

# キューを用意して始点を入れる
Q = deque()
Q.append([sy, sx])
dist[sy][sx] = 0

while len(Q) > 0:
    i, j = Q.popleft()
    # 隣接するマスを確認する
    for i2, j2 in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
        # 盤面の外なら除外
        if not (0 <= i2 < R and 0 <= j2 < C):
            continue

        # 壁なら無視
        if not S[i][j] == "#":
            continue

        # 未訪問なら距離を更新してキューに入れる
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])

print(dist[gy][gx])
