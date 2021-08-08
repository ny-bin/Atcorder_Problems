H, W, N = map(int, input().split())

num_list = []

for n in range(H):
    num_list.append(['*'] * W)

for n in range(N):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    num_list[A][B] = n + 1

for n in range(H):
    count = num_list[n].count('*')
    if count == W:
        num_list[n] = []

for w in range(W):
    new_list = []
    for h in range(H):
        if len(num_list[h]) == 0:
            continue
        else:
            new_list.append(num_list[h][w])

    if new_list.count('*') == len(new_list):
        for h in range(len(new_list)):
            if len(num_list[h]) == 0:
                continue
            else:
                num_list[h][w] = ''

print("a")
