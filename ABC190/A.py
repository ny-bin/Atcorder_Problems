n = input().split()

A = int(n[0])
B = int(n[1])
C = int(n[2])

ans = ''

if C == 0:
    nA = A-1
    if nA >= B:
       ans = 'Takahashi'
    else:
        ans = 'Aoki'
else:
    nB = B - 1
    if A <= nB:
        ans = 'Aoki'
    else:
        ans = 'Takahashi'

print(ans)