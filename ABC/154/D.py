N, K = map(int, input().split())
P = list(map(int, input().split()))

P_handled = []
max_num = 0
for p in P:
    P_handled.append(((p + 1) / 2) * 2)


sum_num = 0
for n in range(len(P_handled)):
    if n < K:
        max_num += P_handled[n]
        sum_num += P_handled[n]
    else:
        sum_num = sum_num + P_handled[n] - P_handled[n - K]
        max_num = max(max_num, sum_num)

print(max_num / 2)
