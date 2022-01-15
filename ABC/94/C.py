N = int(input())
X = list(map(int, input().split()))

Y = sorted(X)

center = len(X) // 2
min_num = Y[center - 1]
max_num = Y[center]

for x in X:
    if x < Y[N // 2]:
        ans = max_num
    else:
        ans = min_num
    print(ans)
