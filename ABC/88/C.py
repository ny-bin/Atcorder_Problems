C = []

for n in range(3):
    num_list = list(map(int, input().split()))
    C.append(num_list)

x = [0] * 3
x[0] = 0
y = [0] * 3
for i in range(3):
    y[i] = C[0][i] - x[0]

for i in range(3):
    x[i] = C[i][0] - y[0]

isGood = True
for i in range(3):
    for j in range(3):
        if C[i][j] != (x[i] + y[j]):
            isGood = False

if isGood:
    print('Yes')
else:
    print('No')
