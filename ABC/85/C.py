N, Y = map(int, input().split())

ans = False
for x in range(N + 1):
    for y in range(N + 1):
        z = N - x - y
        if z < 0:
            continue

        sum_price = 10000 * x + 5000 * y + z * 1000
        if sum_price == Y:
            print(f"{x} {y} {z}")
            ans = True
            break
    if ans:
        break

if not ans:
    print("-1 -1 -1")
