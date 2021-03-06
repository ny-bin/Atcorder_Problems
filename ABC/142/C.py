N = int(input())
num = list(map(int, input().split()))

ans = {}

count = 0
for n in num:
    ans[count] = n
    count += 1


ans_sorted = sorted(ans.items(), key=lambda x:x[1])
for a in ans_sorted:
    print(str(a[0] + 1),end=' ')