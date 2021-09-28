N, T = map(int, input().split())

A = list(map(int, input().split()))

lag = 0
sum_time = 0
before = 0
for a in A:
    if a == 0:
        # スターと
        before = 0
        continue

    lag = a - before
    before = a

    if lag < T:
        # お湯の出る時間の方が長い場合
        sum_time += lag
    else:
        sum_time += T

print(sum_time + T)
