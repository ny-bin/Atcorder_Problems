N, A, X, Y = map(int, input().split())

if N < A:
    print(N * X)
else:
    ans = 0
    ans = X * A + (N - A) * Y
    print(ans)
