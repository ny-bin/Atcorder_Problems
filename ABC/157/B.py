bingo = [list(map(int, input().split())) for n in range(3)]
anslist = [[False,False,False],[False,False,False],[False,False,False]]

ans = "No"

N = int(input())
for n in range(N):
    b = int(input())
    count = 0
    for lis in bingo:
        if b in lis:
            a = lis.index(b)
            anslist[count][a] = True
        count += 1

for i in range(3):
    if (anslist[i][0] and anslist[i][1] and anslist[i][2]):
        ans = "Yes"

for j in range(3):
    if (anslist[0][j] and anslist[1][j] and anslist[2][j]):
        ans = "Yes"

if anslist[0][0] and anslist[1][1] and anslist[2][2]:
    ans = "Yes"

if anslist[0][2] and anslist[1][1] and anslist[2][0]:
    ans = "Yes"

print(ans)