# 数学的解法

# import math

# N = int(input())

# # N番目のゾロ目数の桁数
# x = math.ceil(N / 9)

# # N番目のゾロ目数の数字
# y = N % 9

# if y == 0:
#     y = 9

# ans = ""

# for _ in range(0, x):
#     ans += str(y)

# print(ans)

# 全探索
N = int(input())
z = 0

for i in range(1, 55555 + 1):
    si = str(i)
    ok = True

    for s in si:
        if s != si[0]:
            ok = False

    if ok:
        z += 1
    if ok and z == N:
        ans = i
print(ans)
