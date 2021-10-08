N = int(input())
s = list(input())
t = list(input())

ans = 0
for n in range(N):
    # n文字目から語尾までが重複していると仮定
    split_s = s[n:]
    split_t = t[0:N - n]
    if split_s == split_t:
        ans = len(s) + len(t) - len(split_s)
        break

if ans == 0:
    print(len(s) + len(t))
else:
    print(ans)
