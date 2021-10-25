K, A, B = map(int, input().split())

bisket = 1
money = 0
if B <= A + 1:
    print(K + 1)
elif K <= A:
    print(K + 1)
else:
    while True:
        K -= A
        money += 1
        if K - money < A:
            break

    print((K - money) + (money * B))
