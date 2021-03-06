N = int(input())
num = sorted(list(map(int, input().split())))

mediumNum = 0

for n in num:
    if mediumNum == 0:
        mediumNum = n
    else:
        mediumNum = (n + mediumNum) / 2

print(mediumNum)
