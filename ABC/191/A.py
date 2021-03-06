n = input().split()

A = int(n[0])
B = int(n[1])
C = int(n[2])
D = int(n[3])

ans = ''

if B <= D/A <= C:
    ans = "No"
else:
    ans = "Yes"

print(ans)

