from collections import Counter
n = int(input())

ans = list(input())
for _ in range(n - 1):
    s = list(input())
    ans = list((Counter(ans) & Counter(s)).elements())


ans = sorted(ans)
print("".join(ans))
