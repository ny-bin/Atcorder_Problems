N, K = map(int, input().split())

sum_count = 0

A = []
ans = 0
for n in range(1, N + 1):
    num = n
    count = 0
    while num < K:
        num = num * 2
        count += 1
    A.append(count)

for a in A:
    ans += ((1 / 2) ** a) / N

print(ans)
