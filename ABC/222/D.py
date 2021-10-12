# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# ans = 1

# before_a = 0
# before_b = 0
# for n in range(N):
#     a = A[n]
#     b = B[n]
#     diff = b - a + 1
#     if n != 0:
#         minus = 0
#         for i in range(before_a, before_b + 1):
#             if i <= a:
#                 continue
#             elif i > b:
#                 minus += b - a + 1
#             else:
#                 minus += i - a
#         ans = ((ans * diff) - minus) % 998244353
#     else:
#         ans = ans * diff
#     before_a = a
#     before_b = b

# print(ans)

# i番目がjであるような通り
# P = []
# for n in range(N):
#     P.append([0] * 3000)

# before_a = 0
# before_b = 0
# for i in range(N):
#     a = A[i]
#     b = B[i]
#     for j in range(a, b + 1):
#         if i == 0:
#             P[i][j] = 1
#         else:
#             for k in range(before_a, before_b + 1):
#                 if j >= k:
#                     P[i][j] += P[i - 1][k]
#                 else:
#                     break
#     before_a = a
#     before_b = b

# ans = 0
# for l in range(a, b + 1):
#     ans += P[N - 1][l] % 998244353

# print(ans)

mod = 998244353
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = 3000
dp = [1] * (M + 1)
for i in range(N):
    nx = [0] * (M + 1)
    for j in range(A[i], B[i] + 1):
        nx[j] = dp[j]
    dp = nx
    for i in range(M):
        dp[i + 1] += dp[i]
        dp[i + 1] %= mod
print(dp[M])
