H, W = map(int, input().split())

A = []
for h in range(H):
    a = list(map(int, input().split()))
    A.append(a)

ans = True
for i1 in range(H):
    for i2 in range(H):
        for j1 in range(W):
            for j2 in range(W):
                if i1 >= i2 or j1 >= j2:
                    continue
                else:
                    if A[i1][j1] + A[i2][j2] <= A[i2][j1] + A[i1][j2]:
                        continue
                    else:
                        ans = False
                        break
            if not ans:
                break
        if not ans:
            break
    if not ans:
        break

if ans:
    print('Yes')
else:
    print('No')
