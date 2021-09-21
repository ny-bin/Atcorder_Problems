N, M = map(int, input().split())

students = []
checkpoints = []
for n in range(N):
    a, b = map(int, input().split())
    students.append([a, b])

for m in range(M):
    c, d = map(int, input().split())
    checkpoints.append([c, d])

for n in range(N):
    a, b = students[n]
    min_num = 10 ** 9
    min_point = 0
    for m in range(M):
        # マンハッタン距離を計算
        c, d = checkpoints[m]
        length = abs(a - c) + abs(b - d)
        if min_num == length:
            continue

        min_num = min(min_num, length)

        if min_num == length:
            min_point = m
    print(min_point + 1)
