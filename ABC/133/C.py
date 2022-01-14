L, R = map(int, input().split())

ans = 2019
for i in range(L, R + 1):
    for j in range(L, R + 1):
        if i >= j:
            continue
        num = (i * j) % 2019
        if ans > num:
            ans = num
            if ans == 0:
                break
    if ans == 0:
        break

print(ans)
