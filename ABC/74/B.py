N = int(input())
K = int(input())
nums = list(map(int, input().split()))
ans = 0

for num in nums:
    if K / 2 <= num:
       ans += (K - num) * 2
    else:
        ans += num * 2

print(ans)
