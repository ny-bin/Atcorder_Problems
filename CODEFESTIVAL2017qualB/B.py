N = int(input())
D = list(map(int, input().split()))

M = int(input())
T = list(map(int, input().split()))

ans = True

numdic = {}
for d in D:
    if d in numdic:
        numdic[d] += 1
    else:
        numdic[d] = 1

for t in T:
    if t in numdic and numdic[t] != 0:
        numdic[t] -= 1
    else:
        ans = False

if ans:
    print('YES')
else:
    print('NO')
