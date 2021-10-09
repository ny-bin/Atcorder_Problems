N, M = map(int, input().split())

A = []
for n in range(2 * N):
    a = list(input())
    A.append(a)

P = []
for n in range(2 * N):
    dic = [n, 0]
    P.append(dic)

for m in range(M):
    for n in range(0, 2 * N, 2):
        dic_1_id, dic_1_count = P[n]
        dic_2_id, dic_2_count = P[n + 1]

        p = A[dic_1_id][m]
        q = A[dic_2_id][m]
        if p == q:
            # あいこ
            continue
        elif p == 'G' and q == 'P':
            P[n + 1][1] -= 1
        elif p == 'G' and q == 'C':
            P[n][1] -= 1
        elif p == 'C' and q == 'P':
            P[n][1] -= 1
        elif p == 'C' and q == 'G':
            P[n + 1][1] -= 1
        elif p == 'P' and q == 'G':
            P[n][1] -= 1
        elif p == 'P' and q == 'C':
            P[n + 1][1] -= 1

    P = sorted(P, key=lambda x: (x[1], x[0]))

for p in P:
    print(p[0] + 1)
