from collections import deque
import copy
M = int(input())

map_list = []
for m in range(9):
    map_list.append([])

for m in range(M):
    u, v = map(int, input().split())
    map_list[u - 1].append(v - 1)
    map_list[v - 1].append(u - 1)

pazzle = list(map(int, input().split()))

index = 0
s = list('999999999')
perf = list('123456789')
for p in pazzle:
    a = str(index + 1)
    s[p - 1] = str(index + 1)
    index += 1

Q = deque()

ans = []
mp = {''.join(s): 0}
Q.append((s, 0))
while len(Q) > 0:
    S, count = Q.popleft()
    v = 0
    for i in range(9):
        if S[i] == '9':
            v = i
    for n in map_list[v]:
        t = copy.copy(S)
        c = count
        t[n], t[v] = t[v], t[n]
        c += 1
        if ''.join(t) in mp:
            continue
        else:
            mp[''.join(t)] = c

        if t != perf:
            Q.append((t, c))
        else:
            ans.append(c)

if s == perf:
    print(0)
else:
    if len(ans) == 0:
        print(-1)
    else:
        print(min(ans))
