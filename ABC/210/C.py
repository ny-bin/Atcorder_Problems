import collections

N, K = map(int, input().split())
C = list(map(int, input().split()))

ans = 0
# for n in range(N):
#     sL = C[n:n + K]
#     setNums = list(set(sL))
#     ans = max(ans, len(setNums))
#     if ans == K:
#         break

# print(ans)


sL = C[0:K]
ans = 0
setNums = list(set(sL))
for n in range(K, N):
    ans = max(ans, len(setNums))
    num = C[n]
    if num in setNums:
        break
    else:
        setNums.append()
