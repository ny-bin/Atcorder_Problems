# kn = list(map(int, input().split()))
# K = kn[0]
# N = kn[1]

# ansA = 0
# ansB = 0

# numlist = list(map(int, input().split()))

# mediumPoint = (numlist[0] + numlist[N-1]) / 2


# A = 0
# B = 0
# for n in range(N):
#     if numlist[n] <= mediumPoint <= numlist[n+1]:
#         A = numlist[n]
#         B = numlist[n+1]

# ansA = numlist[N-1] - numlist[0]
# ansB = A + 20 - B

# if ansA < ansB:
#     print(ansA)
# else:
#     print(ansB)

#回答
kn = list(map(int, input().split()))
K = kn[0]
N = kn[1]
numlist = list(map(int, input().split()))
lengthList = []
ans = 0

for n in range(N):
    length = 0
    if n != N - 1:
        length = numlist[n+1] - numlist[n]
    else:
        length = K - numlist[n] + numlist[0]

    lengthList.append(length)

newLen = sorted(lengthList)
for n in range(len(newLen) - 1):
    ans += newLen[n]

print(ans)
