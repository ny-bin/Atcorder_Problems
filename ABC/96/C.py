H, W = map(int, input().split())

map_list = []

for h in range(H):
    str = list(input())
    map_list.append(str)

ans = True
for h in range(H):
    for w in range(W):
        string = map_list[h][w]

        if string == '.':
            continue
        # 左
        if h - 1 >= 0:
            target = map_list[h - 1][w]
            if target == '#':
                continue

        if h + 1 < H:
            target = map_list[h + 1][w]
            if target == '#':
                continue

        if w - 1 >= 0:
            target = map_list[h][w - 1]
            if target == '#':
                continue

        if w + 1 < W:
            target = map_list[h][w + 1]
            if target == '#':
                continue

        ans = False
        break
    if not ans:
        break

if ans:
    print('Yes')
else:
    print('No')
