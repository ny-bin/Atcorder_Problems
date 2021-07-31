import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 10000000000

for a in A:
    mid = bisect.bisect_left(B, a)
    if mid == len(B):
        ans = min(ans, abs(a - B[len(B) - 1]))
        break
    else:
        if mid == 0:
            ans = min(ans, abs(a - B[mid]))
        else:
            ans = min(ans, abs(a - B[mid]), abs(a - B[mid - 1]))

    if ans == 0:
        break

print(ans)
