N = int(input())
C = list(map(int, input().split()))
Q = int(input())

# 合計販売数を記録する
sell = 0

# 全種類販売する枚数
q_3 = 0

# セット販売の枚数
q_2 = 0

# セット販売対象の最小値
min_c_2 = 100000000

# 全販売対象の最小値
min_c_3 = 100000000

for n in range(N):
    if n % 2 == 0:
        min_s_2 = min(C[n], min_s_2)
    else:
        min_s_3 = min(C[n], min_s_3)

for _ in range(0, Q):
    query = map(int, input().split())

    # 単品カードを売る処理
    if query[0] == 1:
        x = query[1] - 1
        s = query[2]
        if x % 2 == 0:
            card_x = C[x] - q_2 - q_3
        else:
            card_x = C[x] - q_3

        if card_x > s:
            C[x] -= s
            sell += s

        if x % 2 == 0:
            min_c_2 = min(C[x], min_c_2)
        else:
            min_c_3 = min(C[x], min_c_3)
    # セット販売
    elif query[0] == 2:
        s = query[1]
        if min_c_2 - q_2 - q_3 - s >= 0:
            q_2 += s
    # 全種類販売
    elif query[0] == 3:
        s = query[1]
        if min(min_s_2 - q_2 - q_3, min_s_3 - q_3) >= s:
            q_3 += s

for i in range(0, N):
    if i % 2 == 0:
        sell += s

sell += q_3 * N
