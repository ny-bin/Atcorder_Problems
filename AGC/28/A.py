import math
N, M = map(int, input().split())
S = input()
T = input()

g = math.gcd(N, M)
ng = N // g
mg = M // g

for i in range(g):
    if S[ng * i] != T[mg * i]:
        print(-1)
        exit()
else:
    print(ng * mg * g)
