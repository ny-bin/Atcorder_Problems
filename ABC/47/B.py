W, H, N = map(int, input().split())
w, h = W, H

xl, xr, yt, yb = 0, W, H, 0
zero_flg = False
for n in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        if xl < x:
            xl = x
    elif a == 2:
        if xr > x:
            xr = x
    elif a == 3:
        if yb < y:
            yb = y
    elif a == 4:
        if yt > y:
            yt = y

    if yt - yb < 0 or xr - xl < 0:
        zero_flg = True
        break

if zero_flg:
    ans = 0
else:
    ans = (yt - yb) * (xr - xl)
print(ans)
