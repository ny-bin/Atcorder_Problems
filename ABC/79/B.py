N = int(input())

L = [0] * 87
L[0] = 2
L[1] = 1

for n in range(N + 1):
    if L[n] != 0:
        continue

    L[n] = L[n - 1] + L[n - 2]

print(L[N])
# ○
