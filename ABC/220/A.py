A, B, C = map(int, input().split())

ans = False
for n in range(A, B + 1):
    if n % C == 0:
        print(n)
        ans = True
        break

if not ans:
    print(-1)
