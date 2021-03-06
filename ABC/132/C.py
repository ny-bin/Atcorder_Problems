N = int(input())
num = sorted(list(map(int, input().split())))

mediumNum = N // 2
ans = 0
if num[mediumNum] == num[mediumNum -1]:
    ans = 0
else:
    ans = num[mediumNum] - num[mediumNum - 1] 

print(ans)