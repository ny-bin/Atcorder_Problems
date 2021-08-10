N, M = map(int, input().split())

L_max = 0
R_min = 100 ** 10

for m in range(M):
    l, r = map(int, input().split())
    L_max = max(l, L_max)
    R_min = min(r, R_min)

if R_min - L_max < 0:
    print(0)
else:
    print(R_min - L_max + 1)
