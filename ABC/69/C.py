s, c = map(int, input().split())

if s * 2 >= c:
    ans = c // 2
else:
    ans = s
    s = 0
    c -= 2 * ans
    ans += c // 4

print(ans)
