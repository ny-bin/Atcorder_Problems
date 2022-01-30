import math


def ceil(x, s):
    return s * math.ceil(x / s)


N = int(input())

A = []
B = []

for n in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

count = 0
for i in range(N - 1, -1, -1):
    count += ceil(A[i] + count, B[i]) - (A[i] + count)

print(count)
