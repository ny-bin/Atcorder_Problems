N = int(input())

map_list = []
for n in range(N):
    mapping = list(map(int, input().split()))
    map_list.append(mapping)

ans = 0
for n1 in range(N):
    for n2 in range(N):
        for n3 in range(N):
            if n1 == n2 or n1 == n3 or n2 == n3:
                continue
            x1, y1 = map_list[n1]
            x2, y2 = map_list[n2]
            x3, y3 = map_list[n3]
            x1 -= x3
            x2 -= x3
            y1 -= y3
            y2 -= y3
            if x1 * y2 != x2 * y1:
                ans += 1

print(ans // 6)
