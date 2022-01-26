import math


N = int(input())

A = list(map(int, input().split()))

ans = 0
for a in A:
    ans = math.gcd(ans, a)

print(ans)
