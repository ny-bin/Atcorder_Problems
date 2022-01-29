N = int(input())
A = list(map(int, input().split()))

num_dic = {}
for a in A:
    if a in num_dic:
        num_dic[a] += 1
    else:
        num_dic[a] = 1

ans = 0

for i in num_dic:
    count = num_dic[i]
    if i > count:
        ans += count
    elif i < count:
        ans += count - i

print(ans)
