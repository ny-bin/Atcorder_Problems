W, H, x, y = map(int, input().split())

print((W * H) / 2, end=' ')

if x + x == W and y + y == H:
    print(1)
else:
    print(0)
