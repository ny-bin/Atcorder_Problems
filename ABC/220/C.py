N = int(input())
A = list(map(int, input().split()))
X = int(input())

sum_A = sum(A)

ans = 0


x = X
if sum_A > X:
    for a in A:
        X -= a
        ans += 1
        if X < 0:
            print(ans)
            break
else:
    count = X // sum_A
    X = X % sum_A
    ans += count * N
    if X == 0:
        print(ans + 1)
    else:
        for a in A:
            X -= a
            ans += 1
            if X < 0:
                print(ans)
                break
