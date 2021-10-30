N = int(input())

ans = False
count_list = [0] * N
for n in range(N - 1):
    a, b = map(int, input().split())
    count_list[a - 1] += 1
    count_list[b - 1] += 1

for count in count_list:
    if count == N - 1:
        ans = True

if ans:
    print('Yes')
else:
    print('No')
