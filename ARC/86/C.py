N, K = map(int, input().split())

A = list(map(int, input().split()))

num_dic = {}

for a in A:
    if a in num_dic:
        num_dic[a] += 1
    else:
        num_dic[a] = 1

num_count = len(num_dic)
ans = 0
if num_count <= K:
    print(ans)
else:
    sorted_dic = sorted(num_dic.items(), key=lambda x: x[1])
    for n in range(num_count - K):
        ans += sorted_dic[n][1]

    print(ans)
