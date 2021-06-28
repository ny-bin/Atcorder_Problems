# 再帰の上限を増やす
import sys
sys.setrecursionlimit(1000000)

H, W = list(map(int, input().split()))
S = []
sy, sx = 0, 0
gy, gx = 0, 0

for h in range(H):
    s = input()
    S.append(s)

for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            sy = i
            sx = j
        if S[i][j] == "g":
            gy = i
            gx = j


# 訪問済みかどうかの判定
visited = []

for i in range(H):
    visited.append([False] * W)


# 再帰関数の定義
def dfs(i, j):
    for i2, j2 in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
        if not (0 <= i2 < H and 0 <= j2 < W):
            continue

        if S[i][j] == "#":
            continue

        if not visited[i2][j2]:
            dfs(i2, j2)


dfs(sy, sx)

if visited[gy][gx]:
    print("Yes")
else:
    print("No")
