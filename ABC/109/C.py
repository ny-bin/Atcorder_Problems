import math

N, X = map(int, input().split())
L = list(map(int, input().split()))

gcd = 0
for l in L:
    # start地点との距離を測定
    length = abs(X - l)
    if length == 0:
        gcd = length
    else:
        gcd = math.gcd(gcd, length)

print(gcd)
