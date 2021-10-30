N, M = map(int, input().split())

B = []
for n in range(N):
    b = list(map(int, input().split()))
    B.append(b)

ans = True
b_zero_before = 0
b_before = 0
for n in range(N):
    b_zero = B[n][0]
    remainder = b_zero % 7
    if remainder == 0:
        remainder = 7
    if remainder + (M - 1) > 7:
        ans = False

    if n == 0:
        b_zero_before = B[n][0]
    else:
        if b_zero_before + 7 != B[n][0]:
            ans = False
            break
        else:
            b_zero_before = b_zero

    b_before = 0
    for m in range(M):
        b = B[n][m]
        if m == 0:
            b_before = B[n][m]
        else:
            if b_before + 1 != b:
                ans = False
            else:
                b_before = b


if ans:
    print('Yes')
else:
    print('No')
