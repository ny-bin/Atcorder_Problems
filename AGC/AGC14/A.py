num = list(map(int, input().split()))

A = num[0]
B = num[1]
C = num[2]
ans = 0
while True:
    if A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        a = B / 2 + C / 2
        b = A / 2 + C / 2
        c = A / 2 + B / 2
        if c in num and b in num and a in num:
            ans = -1
            break
        else:
            ans += 1
            A = a
            B = b
            C = c
            num = [A, B, C]
    else:
        break

print(ans)
