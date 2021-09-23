H, W = map(int, input().split())

A = []
for h in range(H):
    a = input()
    A.append(a)

while True:
    # 横を見る
    wid_remove = False
    heigh_remove = False
    for h in range(len(A)):
        a_wid = A[h]
        if "#" not in a_wid:
            A.remove(a_wid)
            wid_remove = True
            break

    # 縦を見る
    for w in range(len(A[0])):
        isDel = True
        heigh_remove = True
        for h in range(len(A)):
            a = A[h][w]
            if a == '#':
                isDel = False
                heigh_remove = False

        if isDel:
            for h in range(len(A)):
                A[h] = A[h][:w] + A[h][w + 1:]
            break
    if not wid_remove and not heigh_remove:
        break


for a in A:
    print(a)
