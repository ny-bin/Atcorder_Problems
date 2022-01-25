

S = input()
Q = int(input())

reverse_flg = False
pre_str = []
end_str = []
for q in range(Q):
    query = list(input().split())
    t = query[0]
    if t == "1":
        reverse_flg = not reverse_flg
    else:
        f = query[1]
        c = query[2]
        if f == "1" and not reverse_flg:
            pre_str.append(c)
        elif f == "1" and reverse_flg:
            end_str.append(c)
        elif f == "2" and not reverse_flg:
            end_str.append(c)
        else:
            pre_str.append(c)

ans = ""
if not reverse_flg:
    for i in range(len(pre_str) - 1, -1, -1):
        ans += pre_str[i]
    ans += S
    for n in end_str:
        ans += n
else:
    for i in range(len(end_str) - 1, -1, -1):
        ans += end_str[i]
    for i in range(len(S) - 1, -1, -1):
        ans += S[i]
    for n in pre_str:
        ans += n

print(ans)
