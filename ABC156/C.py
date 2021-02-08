N = int(input())
X = sorted(list(map(int, input().split())))
dp = {}
ans = 100000000

for i in range(X[0], X[N-1], 1):
    sum_length = 0
    for n in range(N):
        length = abs(i - X[n])
        if length in dp:
            sum_length += dp[length]
        else:
            dp[length] = length ** 2
            sum_length += dp[length]
    
    if sum_length < ans:
        ans = sum_length

if ans == 100000000:
    ans = 0
print(ans)

