N = int(input())
A = list(map(int, input().split()))

y = sum(A)
ans = 10 ** 10
x = 0
for a in range(len(A) - 1):
    x += A[a]
    y -= A[a]

    ans = min(ans, abs(x - y))

print(ans)
