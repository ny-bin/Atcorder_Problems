x, y = map(int, input().split())

ans = 0
if x * y > 0:
    if y - x > 0:
        ans = y - x
    else:
        ans = (x - y) + 2
elif x * y == 0:
    if x == 0 and y < 0:
        ans = abs(y) + 1
    elif y == 0 and x < 0:
        ans = abs(x)
    elif x == 0 and y > 0:
        ans = y
    elif y == 0 and x > 0:
        ans = x + 1
else:
    if x < 0:
        ans = abs(y - (-1 * x)) + 1
    else:
        ans = abs((-1 * y) - x) + 1

print(ans)
