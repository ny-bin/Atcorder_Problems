N, K = map(int, input().split())
C = list(map(int, input().split()))

# for n in range(N):
#     sL = C[n:n + K]
#     setNums = list(set(sL))
#     ans = max(ans, len(setNums))
#     if ans == K:
#         break

# print(ans)


# sL = C[0:K]
# ans = 0
# setNums = list(set(sL))
# for n in range(K, N):
#     ans = max(ans, len(setNums))
#     num = C[n]
#     if num in setNums:
#         break
#     else:
#         setNums.append()

dic = {}
first = []
ans = 0

for n in range(N):
    target = C[n]
    if n < K:
        if target in dic:
            dic[target] += 1
        else:
            dic[target] = 1
        ans = max(len(dic), ans)
        continue
    else:
        if target in dic:
            dic[target] += 1
        else:
            dic[target] = 1

    del_num = C[n - K]
    if del_num in dic:
        dic[del_num] -= 1
    if dic[del_num] == 0:
        del dic[del_num]
    ans = max(len(dic), ans)

print(ans)
