N, M = map(int, input().split())
X = sorted(map(int, input().split()))
X_minus = []
if M - N <= 0:
    print(0)
else:
    for x in range(len(X)):
        if x != len(X) - 1:
            X_minus.append(X[x + 1] - X[x])

    X_minus.sort()
    ans_list = X_minus[0:len(X) - N]

    print(sum(ans_list))

# ○
