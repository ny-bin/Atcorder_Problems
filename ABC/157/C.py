N, M = map(int, input().split())

A = [0] * N

ans = 0
for m in range(M):
    s, c = map(int, input().split())
    a = A[s - 1]
    if a != 0 and a != c:
        ans = -1
        break
    A[s - 1] = c

if ans != -1:
    a = A[0]
    if a == 0:
        ans = -1

    for n in range(len(A)):
        a = A[n]
        ans += A[n] * (10 ** (len(A) - (n + 1)))


print(ans)
