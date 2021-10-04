N, M = map(int, input().split())

L = []
for m in range(M):
    sc = list(map(int, input().split()))
    L.append(sc)


ans = -1
for n in range(10 ** N + 1):
    numStr = str(n)
    if len(numStr) != N:
        continue

    isok = True
    for m in L:
        if numStr[m[0] - 1] == str(m[1]):
            continue
        else:
            isok = False
            break

    if isok:
        ans = n
        break

print(ans)
