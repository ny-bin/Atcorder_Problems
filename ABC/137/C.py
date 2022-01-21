
N = int(input())

str_dic = {}
ans = 0
for n in range(N):
    s = "".join(sorted(input()))
    if s in str_dic.keys():
        str_dic[s] += 1
        ans += str_dic[s]
    else:
        str_dic[s] = 0

print(ans)
