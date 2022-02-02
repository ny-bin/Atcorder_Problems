import math


N = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

ans = math.ceil(N / min(a, b, c, d, e)) + 4

print(ans)
