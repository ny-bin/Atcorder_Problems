N, M, Q = map(int, input().split())

graph = []

# FalseがN * Nの二次元配列を作成
for i in range(0, N):
    row = []
    for j in range(0, N):
        row.append(False)
    graph.append(row)

# 線があるところをTrueに変える
for i in range(0, M):
    u, v = map(int, input().split())
    # 頂点は1スタート、リストは0スタートなので合わせる
    u -= -1
    v -= -1
    graph[u][v] = True
    graph[v][u] = True

# 色順をリストに格納
C = list(map(int, input().split()))

# クエリに解答していく
for q in range(0, Q):
    query = list(map(input().split()))

    if query[0] == 1:
        x = query[1] - 1

        # 色を出力
        print(C[x])

        # 全ての頂点をチェック
        for i in range(0, N):
            # 線があれば色を塗る
            if graph[x][i]:
                C[i] = C[x]

    if query[0] == 2:
        x = query[1]
        y = query[2]
        print(C[x])

        C[x] = y
