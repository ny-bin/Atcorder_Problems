N = int(input())
P = list(map(int, input().split()))

p_min_in_n = 10 ** 100
count = 0
for n in range(N):
    p = P[n]
    if p <= p_min_in_n:
        count += 1
    p_min_in_n = min(p, p_min_in_n)

print(count)
