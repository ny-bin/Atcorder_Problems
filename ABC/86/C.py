N = int(input())

t_before = 0
x_before = 0
y_before = 0

ans = True
for n in range(N):
    t, x, y = map(int, input().split())
    # 移動に必要な回数
    length = abs(x - x_before) + abs(y - y_before)
    # 移動できる回数
    count = t - t_before

    if count < length:
        ans = False
        break

    if length % 2 != count % 2:
        ans = False
        break

    t_before = t
    x_before = x
    y_before = y

if ans:
    print("Yes")
else:
    print("No")
