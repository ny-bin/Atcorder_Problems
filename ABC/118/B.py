N, M = map(int, input().split())

com_list = []
for n in range(N):
    ak = list(map(int, input().split()))
    k = ak[0]
    A = ak[1:]
    if n == 0:
        for a in A:
            com_list.append(a)
    else:
        dellist = []
        for com in com_list:
            if com not in A:
                dellist.append(com)
        for delNum in dellist:
            com_list.remove(delNum)

print(len(com_list))
