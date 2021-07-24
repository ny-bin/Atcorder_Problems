from collections import deque

N, M = map(int, input().split())

G = []
for _ in range(0, N):
    G.append([])

for m in range(M):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1
    G[ai].append(bi)
    G[bi].append(ai)

dist = []
cnt = [0] * N
for _ in range(0, N):
    dist.append(-1)
dist[0] = 0
cnt[0] = 1

Q = deque()
Q.append(0)

while len(Q) > 0:
    i = Q.popleft()
    for j in G[i]:
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            cnt[j] += 1
            cnt[j] %= (10 ** 9 + 7)
            Q.append(j)
        elif dist[j] == dist[i] + 1:
            cnt[j] += 1
            cnt[j] %= (10 ** 9 + 7)
            Q.append(j)

print(cnt[N - 1])
