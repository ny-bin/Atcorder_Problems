bingo = []
M = [[False, False, False], [False, False, False], [False, False, False]]

# ビンゴを作成
for n in range(3):
    bingo.append(list(map(int, input().split())))

# 数字がビンゴに含まれているかを確認
N = int(input())
for n in N:
    num = int(input())

    for i in range(0, 3):
        for j in range(0, 3):
            if bingo[i][j] == num:
                M[i][j] = True

# ビンゴを達成しているか調べる
bingo = False
for i in range(0, 3):
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

for i in range(0, 3):
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True


if M[0][0] and M[1][1] and M[2][2]:
    bingo = True

if M[2][0] and M[1][1] and M[2][0]:
    bingo = True

if bingo:
    print("Yes")
else:
    print("No")
