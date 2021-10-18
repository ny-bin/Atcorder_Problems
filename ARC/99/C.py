import math
N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = math.ceil((N - 1) / (K - 1))
print(ans)
# ans = (N - 1 + K - 2) // (K - 1)
# print(ans)

# △
# 10/19 解き直し○
