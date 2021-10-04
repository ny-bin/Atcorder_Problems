N, A, B = map(int, input().split())

if A == B:
    print(1)
elif B < A:
    print(0)
else:
    if N == 1:
        print(0)
    else:
        count = N - 2
        ans = (B * count) - (A * count) + 1
        print(ans)
