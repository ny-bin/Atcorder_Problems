N = int(input())

all_ten = True

min_num = 101
ans = 0
for n in range(N):
    s = int(input())
    if s % 10 != 0:
        all_ten = False
        min_num = min(s, min_num)
    ans += s

if all_ten:
    print(0)
else:
    if ans % 10 == 0:
        print(ans - min_num)
    else:
        print(ans)
