N, C, K = map(int, input().split())

T = []
for n in range(N):
    a = int(input())
    T.append(a)

T = sorted(T)

B = []
ans = 0
for i in range(len(T)):
    t = T[i]
    if len(B) > 0:
        first = B[0]
        if t - first <= K:
            B.append(t)
        else:
            ans += 1
            B = []
            B.append(t)
            continue
    else:
        B.append(t)

    if len(B) == C:
        ans += 1
        B = []
        continue

if len(B) > 0:
    ans += 1
print(ans)
