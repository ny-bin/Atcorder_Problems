H, W = map(int, input().split())

bom_map = []
ans = []
for h in range(H):
    S = input()
    bom_map.append([])
    ans.append([])
    for s in S:
        bom_map[h].append(s)
        ans[h].append('')


for h in range(H):
    for w in range(W):
        if bom_map[h][w] == '#':
            ans[h][w] = '#'
            continue

        count = 0
        # 上
        if h - 1 >= 0:
            if bom_map[h - 1][w] == '#':
                count += 1
        # 下
        if h + 1 < H:
            if bom_map[h + 1][w] == '#':
                count += 1

        # 左
        if w - 1 >= 0:
            if bom_map[h][w - 1] == '#':
                count += 1

        # 右
        if w + 1 < W:
            if bom_map[h][w + 1] == '#':
                count += 1

        # 右上
        if h - 1 >= 0 and w + 1 < W:
            if bom_map[h - 1][w + 1] == '#':
                count += 1

        # 左上
        if h - 1 >= 0 and w - 1 >= 0:
            if bom_map[h - 1][w - 1] == '#':
                count += 1

        # 左下
        if h + 1 < H and w - 1 >= 0:
            if bom_map[h + 1][w - 1] == '#':
                count += 1

        # 右下
        if h + 1 < H and w + 1 < W:
            if bom_map[h + 1][w + 1] == '#':
                count += 1

        ans[h][w] = str(count)

for h in range(H):
    print(''.join(ans[h]))
