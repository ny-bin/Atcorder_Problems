import math


def lcm(a, b):
    y = a * b // math.gcd(a, b)
    return y


N = int(input())

ans = 1
for n in range(N):
    t = int(input())
    ans = lcm(ans, t)

print(ans)
