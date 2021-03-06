nmx = list(map(int, input().split()))
#ゴール
N = nmx[0]
#料金所の個数
M = nmx[1]
#スタート地点
X = nmx[2]

num = list(map(int, input().split()))


count1 = 0
count2 = 0
ans = 0

startindex = 101
for i in range(len(num)):
    if num[i] < X < num[i + 1]:
        startindex = i

if startindex == 101:
    print(0)
else:
    for j in range(0, startindex + 1, 1):
        count1 += 1

    for k in range(startindex + 1, len(num), 1):
        count2 += 1

    if count1 < count2:
        ans = count1
    else:
        ans = count2

    print(ans)
