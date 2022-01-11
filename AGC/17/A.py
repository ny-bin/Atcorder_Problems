N, P = map(int, input().split())
A = list(map(int, input().split()))
A_rest = [a % 2 for a in A]

one_count = A_rest.count(1)
zero_count = A_rest.count(0)

if one_count > 0:
    ans = (2 ** (one_count - 1)) * (2 ** zero_count)
else:
    if P == 0:
        ans = 2 ** zero_count
    else:
        ans = 0
print(ans)
