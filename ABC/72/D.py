N = int(input())

P = list(map(int, input().split()))

X = []
for i in range(N):
    if i + 1 == P[i]:
        X.append("x")
    else:
        X.append("o")

ans = 0
for j in range(N):
    x = X[j]
    if x == "x":
        ans += 1
        X[j] = "o"
        if j == N - 1:
            continue
        if X[j + 1] == "x":
            X[j + 1] = "o"

print(ans)
