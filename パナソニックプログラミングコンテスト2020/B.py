num = list(map(int, input().split()))
H = num[0]
W = num[1]
w = 0
h = 0
ans = 0
if H == 1 or W == 1:
    ans = 1
else:
    if W % 2 == 0:
        ans = (W / 2) * (H)
    else:
        w = W // 2 + 1
        if H % 2 == 0:
            ans = (w * (H/2)) + ((w-1) * (H/2))
        else:
            ans = (w * (H//2 + 1)) + ((w-1) * (H//2))

print(int(ans))
