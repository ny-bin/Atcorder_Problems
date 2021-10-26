K, A, B = map(int, input().split())

bisket = 1
money = 0
if B - A <= 2:
    print(K + 1)
else:
    # 交換可能回数
    count = max(0, (K - A + 1) // 2)
    ans = A + ((B - A) * count)
    if (K - A + 1) % 2 == 1:
        ans += 1
    print(ans)
# ×
