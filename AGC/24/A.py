A, B, C, K = map(int, input().split())
ans = 0
if K == 0 or K % 2 == 0:
    ans = (A - B)
else:
    ans = (B - A)

print(ans)
# ○
